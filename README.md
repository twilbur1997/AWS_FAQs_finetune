# Fine Tuning with Custom Prompts

SageMaker JumpStart models offer the ability to be fine tuned using your own data in the form of custom prompts. 

# How to Create Custom Prompts

The prompts are found in the file data.jsonl. This file is needed to fine tune the model

From SageMaker JumpStart:

*A folder containing the data in a JSON lines file data.jsonl and (optionally) prompt template in a JSON file template.json:*

*If no prompt template is provided, the entries of data.jsonl must be of the format {'prompt': <string>, 'completion': <string>}*

*Else the template must have the keys 'prompt' and 'completion' and the values are strings how those are formed via the data keys. For details please look at the default data set.*

*Validation data can be separately provided. If no validation data is given, the training data is split into a training and validation set.*

# What is JSONL?

JSONL is a type of JSON called JSON Lines. It's just a bit more strict (and readable) than JSON can sometimes be. Here's an example (taken from here<https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker_processing/spark_distributed_data_processing/data/data.jsonl>):

`
{"date":"2020-01-04","sale":283}   \n
{"date":"2020-01-06","sale":140}   \n
{"date":"2020-01-05","sale":820}   \n
{"date":"2020-01-04","sale":452}   \n
{"date":"2020-01-06","sale":495}   \n
`

For SageMaker JumpStart, the file would look similar to the following:


`
{"prompt":"What is the first letter of the alphabet?","completion":"The first letter of the alphabet is A."}  \n  
{"prompt":"Where is Silicon Valley?","completion":"Silicon Valley is located in the Southern Bay Area of California."}  \n  
{"prompt":"How long is a marathon?","completion":"A marathon is 26.2 miles."}  \n  
{"prompt":"What is the freezing temperature of water?","completion":"Water freezes at 32 degrees Fahrenheit, which is the same as 0 degrees Celsius"}  \n  
{"prompt":"What is XKCD?","completion":"XKCD is a webcomic written and illustrated by Randall Munroe"}  \n  
`