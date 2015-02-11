from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=128, unique = True)

    def __unicode__(self):
        return self.name

class Match(models.Model):
    player_1_id = models.ForeignKey(Player, null=True, related_name="player_1")
    player_2_id = models.ForeignKey(Player, null=True, related_name="player_2")
    player_1_score = models.IntegerField(default=0)
    player_2_score = models.IntegerField(default=0)
    date = models.DateField()

    def __unicode__(self):
        return "{} vs {} : {} to {}".format(self.player_1_id.name, self.player_2_id.name, self.player_1_score, self.player_2_score)


