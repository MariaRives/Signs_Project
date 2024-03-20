from django.db import models

# Create your models here.

class Subject(models.Model):
    class Genders(models.TextChoices):
        FEMALE = 'Female'
        MALE = 'Male'
        OTHER = 'Other'

    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices= Genders.choices)
    nationality = models.CharField(max_length=25)
    driversLicense = models.CharField(max_length=15)
    yearsXP = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.age}, {self.driversLicense}"

class Signal (models.Model):
    class SignalType(models.TextChoices):
        SYMBOL = 'Symbol'
        TEXT = 'Text'
        BOTH = 'Both'
        TRAINING = 'Training'
        PREFERENCE = 'Preference'

    class Frequencies (models.TextChoices):
        COMMON = "Common"
        UNCOMMON = "Uncommon"

    description = models.CharField(max_length=25)
    signalType = models.CharField(max_length=10, choices= SignalType.choices)
    frequency = models.CharField(max_length=8, choices= Frequencies.choices)
    imgURL = models.CharField(max_length=500)

    def serialize (self):
        return{
            "id": self.id,
            "description": self.description,
            "signalType": self.signalType,
            "frequency": self.frequency,
            "imgURL": self.imgURL
        }

    def __str__(self) -> str:
        return f"{self.description} - {self.frequency} - {self.signalType}"
    
class Reaction_Time (models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="ReactionTimes")
    signal = models.ForeignKey(Signal, on_delete=models.CASCADE, related_name="ReactionTimes")
    reactionTime = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.subject} - ({self.signal}) - {self.reactionTime}ms"
    
class Preference (models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="Preferences")
    signal = models.ForeignKey(Signal, on_delete=models.CASCADE, related_name="Preferences")
    class SignalType(models.TextChoices):
        SYMBOL = 'Symbol'
        TEXT = 'Text'
        BOTH = 'Both'

    preference = models.CharField(max_length=8, choices= SignalType.choices)

class Identify (models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="guesses")
    signal = models.ForeignKey(Signal, on_delete=models.CASCADE, related_name="guesses")
    guess = models.CharField(max_length=25)

class Importance (models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="Importances")
    signal = models.ForeignKey(Signal, on_delete=models.CASCADE, related_name="Importances")
    class ImportanceValues(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        
    importance = models.IntegerField(default=ImportanceValues.FIVE, choices=ImportanceValues.choices)
