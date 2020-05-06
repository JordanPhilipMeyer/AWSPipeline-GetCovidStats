# AWSPipeline-GetCovidStats

This is lambda code to get public covid data and push to dynamodb. This code grabs data from a public URL, reorganizes the structure, and then pushes to dynamodb.

  1. Set up a dynamodb: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SettingUp.html

  2. Prep code

  3. Once your code is ready, you should follow the AWS instructions to zip and push the code into lambda: https://aws.amazon.com/premiumsupport/knowledge-center/build-python-lambda-deployment-package/

  4. Save and run lambda test to see if properly set up.
