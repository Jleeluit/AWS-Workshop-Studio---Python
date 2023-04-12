import json

# This uses a json string as an input 

json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]
}
"""

def main():
    json_input = json.loads(json_string)
    print(json_input)

if __name__=="__main__":
    main()
