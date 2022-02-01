import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Ad(models.Model):
    """
    This is a basic Ad with the most general information people may need/give.
    
    Individual needs, puposes and goals of people who post ads may differ.
    But this class should cover all basic information which would otherwise cause repetition in classes which inherit from this Ads()-class.
    """
    def __str__(self) -> str:
        return self.projectTitle

    #project title
    projectTitle = models.CharField(max_length=100)

    # user account and name of ad creator
    # adCreator = #TODO: define a user here
    # real name or nick name of the ad creator (for now - as long as no user account functionality set up)
    creatorName = models.CharField(max_length=50)

    #project description
        #purpose of ad - What is you goal for your project? What are your searching for? What do you need?
    projectDescription = models.TextField(max_length=1500)

    #contact details of ad creator - How, Where to ad creator
    contactDetails = models.CharField(max_length=300)

    #creation date of ad
    pubDate = models.DateTimeField('publication date (of ad)', auto_now_add=True, blank=True) #publication date should not be editable

    #TODO: (start date of project - When did you start with the project?)
    projectStartDate = models.DateField('project started (date)', blank=True) #start date should be editable by creator

    #(location - Where are you planning to meet for the development of this project? -> should ideally be remote!?)

    #TODO: expiration date of ad (may not be visible - but important for backend/database purposes)
        #TODO: users should receive email notification one week before expiration (to have the chance to extend ads' expiration date by another month)
    #projectStartDate + 30 days (may use timedelta)
    expirationTime = models.DateTimeField('expiration time (of ad)', default=timezone.now() + datetime.timedelta(days=30))
        #TODO: delete ad automatically when expiration time is now

    #publishedRecently (function from djangoDocsTutorial: https://docs.djangoproject.com/en/4.0/intro/tutorial02/#playing-with-the-api)
    def publishedRecently(self):
        return self.pubDate >= timezone.now() - datetime.timedelta(days=1)

    #(like - How many people have clicked the like button?)
    likes = models.IntegerField(default=0)

    #...


#comment class (just to have a model which relates to the Ad model like "Question" & "Choice" in djangoDocsTutorial)
class Comment(models.Model):
    """
    This class provides the opportunity to comment on certain projects...
    """
    def __str__(self) -> str:
        return self.ad.projectTitle[:10] + ' | ' + self.commentText[:20]    #TODO: return statement may be adjusted to display helpful identifier for comment in django admin

    #many-to-one relation to certain Ad (many comment may be connected to one question)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE) #comments/discussion on this project (May be discarded once application goes live, to avoid discussions and to ensure calssifieds character instead of twitter-like behavior...)
    
    # comment =
    #TODO: implement many-to-one relation between this comment and all the comments below (this one comment may have many subcomments=replies)
    #       alternative: include disqus frame instead of building your own commenting system(?)
    
    #text of comment
    commentText = models.TextField(max_length=1000)

    #user who wrote that comment
    #TODO: create user accounts and relation!?

    #pubDate (When was this comment published?)
    pubDate = models.DateTimeField('publication date (of comment)', auto_now_add=True, blank=True) #publication date should not be editable

    #comments (comments by other users on that comment)
    #TODO: build a many-to-one relationship between certain comments?!

    #likes (count likes which users give to that comment)
    likes = models.IntegerField(default=0)


#PresenterAd inherits from general Ad() an adds additional features
class PresenterAd(Ad):
    """
    Ads of this class are meant for people who built their own projects and want to present them for certain reasons.
    
    These people may be experienced developers or even coding beginners.
    But at least they have enough coding experience to having started a project on their own.
    
    possible reasons (needs)
    ----------
    - seeking feedback
    - seeking help (since they got stuck on a certain topic)
    - building a team to work on their project together
    - ...
    """
    def __str__(self) -> str:
        return self.projectTitle


#SpecialistAd for experienced developers who provide help on "special" topics
class SupporterAd(Ad):
    """
    Ads of this class are meant for developers who specialize on certain topics (f.ex. frontend, backend, DevOps, or even certain languages or frameworks).

    possible reasons (needs):
    ----------
    - join people/teams with great project ideas to develop projects together
    - support people who are just starting
    - building a team to work on others projects together
    """
    def __str__(self) -> str:
        return self.projectTitle