from django.test import TestCase
from jobs.models import Jobs
from django.utils import timezone
# Create your tests here.

class JobsTestCase(TestCase):
    def setUp(self):
        Jobs.objects.create(
        job_title="this_is_test_job",
        job_descripttion="dfgsdfgsdfgsdfg",
        create_on="2018-10-09",
        closed_on="2018-10-09",)

    def test_create_job(self):
        """Animals that can speak are correctly identified"""
        job_detail = Jobs.objects.get(job_title="this_is_test_job")
        print ("job_detail==>{}".format(job_detail.job_descripttion))
        import pprint
        pprint.pprint(job_detail)
        # cat = Job.objects.get(name="cat")
        # self.assertEqual(lion.speak(), 'The lion says "roar"')
        # self.assertEqual(cat.speak(), 'The cat says "meow"')
