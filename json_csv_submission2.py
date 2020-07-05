import pandas as pd
import os
import json

Image = []
Target = []
# put the json file with complete path here
with open('dance_result.json') as f:
    data = json.load(f)
    for element in data:
        file = os.path.basename(element['filename'])
        Image.append(file)
        max_confidence = 0
        target_with_high_confidence = ''

        if element['objects']:
            for i in range(len(element['objects'])):
                if element['objects'][i]['confidence'] > max_confidence:
                    # print(element['frame_id'])
                    max_confidence = element['objects'][i]['confidence']
                    target_with_high_confidence = element['objects'][i]['name']

            Target.append(target_with_high_confidence)
        else:
            print(element['frame_id'])
            Target.append('manipuri')
# print(len(Image))
# print(len(Target))

# generate the final submission file here
submission_df = pd.DataFrame({'Image': Image, 'Target': Target})
#print(submission_df.head())
submission_df.to_csv("Submission.csv", index=False)
