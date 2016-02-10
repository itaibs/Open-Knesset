# encoding: utf-8
from knesset_data.dataservice.votes import Vote as DataserviceVote, VoteMember as DataserviceVoteMember
from knesset_data.html_scrapers.votes import HtmlVote
from laws.models import Vote, VoteAction
from simple.scrapers import hebrew_strftime
from simple.scrapers.management import BaseKnessetDataserviceCollectionCommand
from mks.models import Member
from simple.management.commands.syncdata import Command as SyncdataCommand


class Command(BaseKnessetDataserviceCollectionCommand):

    DATASERVICE_CLASS = DataserviceVote

    help = "Scrape latest votes data from the knesset"

    def _has_existing_object(self, dataservice_vote):
        qs = Vote.objects.filter(src_id=dataservice_vote.id)
        return qs.exists()

    def _create_new_object(self, dataservice_vote):
        vote = Vote.objects.create(
            src_id=dataservice_vote.id,
            title=u'{vote} - {sess}'.format(vote=dataservice_vote.item_dscr, sess=dataservice_vote.sess_item_dscr),
            time_string = u'יום '+hebrew_strftime(dataservice_vote.datetime),
            importance = 1,
            time = dataservice_vote.datetime,
            meeting_number = dataservice_vote.session_num,
            vote_number = dataservice_vote.nbr_in_sess,
            src_url = dataservice_vote.id
        )
        for member_id, vote_result_code in HtmlVote.get_from_vote_id(dataservice_vote.id).member_votes:
            member_qs = Member.objects.filter(pk=member_id)
            if member_qs.exists():
                member = member_qs.first()
                vote_type = {
                    'voted for': u'for',
                    'voted against': u'against',
                    'abstain': u'abstain',
                    'did not vote': u'no-vote',
                }[vote_result_code]
                vote_action, created = VoteAction.objects.get_or_create(vote = vote, member = member, defaults={'type':vote_type, 'party':member.current_party})
                if created:
                    vote_action.save()
            else:
                raise Exception('vote %s: could not find member id %s'%(dataservice_vote.id, member_id))
        vote.update_vote_properties()
        SyncdataCommand().find_synced_protocol(vote)
        return vote
        # if v.full_text_url != None:
        #     l = Link(title=u'מסמך הצעת החוק באתר הכנסת', url=v.full_text_url, content_type=ContentType.objects.get_for_model(v), object_pk=str(v.id))
        #     l.save()
