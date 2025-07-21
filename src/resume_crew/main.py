#!/usr/bin/env python
import sys
import warnings

from resume_crew.crew import ResumeCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the resume optimization crew.
    """
    inputs = {
        'job_url': 'https://www.linkedin.com/jobs/view/4229485884/?trackingId=kr%2Far5pcBn23nzYytVbULw%3D%3D&refId=ByteString%28length%3D16%2Cbytes%3Db8fe116f...1b0b909b%29&midToken=AQEyNCZy05ip9Q&midSig=0l9FzvO9J8QHQ1&trk=eml-email_job_alert_digest_01-primary_job_list-0-jobcard_body_4511694433&trkEmail=eml-email_job_alert_digest_01-primary_job_list-0-jobcard_body_4511694433-null-2sgis7~mdc3f8zi~vz-null-null&eid=2sgis7-mdc3f8zi-vz&otpToken=MTMwMzE2ZTcxMTJjY2RjN2JkMjQwNGVkNDMxZGU3YjA4ZWNmZDI0NDk4YWU4OTYxNzRjMDA4NjY0YTUzNWZmNWZlZGY5MmFiNTVkN2ZiODE2MzhkZjE0NjJlMjZiYzMyOTRlNWQyMWU3NzQ1Njg3YjFjNzQsMSwx',
        'company_name': 'CoreWeave'
    }
    ResumeCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
