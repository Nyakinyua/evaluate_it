from django.test import TestCase
from .models import User_profile,Projects
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTestClass(TestCase):
    #set up method
    def setUp(self):
        self.joyce = User(username="Joyce", email="jayjoys968@gmail.com")
        self.joyce = User_profile(user=self.joyce,bio="chill pill",profile_pic="joy.jpg",email="jayjoys968@gmail.com",phone_number='0721222324')
        
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.joyce,User_profile))

    #Testing save method
    def test_save_profile(self):
        self.save_profile()
        profile = User_profile.object.filter(id=user_id)
        self.assertTrue(len(profile)>0)
        
    # Testing delete method
    def test_delete_profile(self):
        self.maya.delete_profile()
        profiles = Profile.objects.all()
        self.assertEqual(len(profiles), 0)
        
