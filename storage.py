import json

FILE = "tasks.json"
 

def load_tasks():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
        
        if isinstance(data, list):
            return {
                "pending": data,
                "completed": []
            }
        return data 
    
    except:
        return{
            "pending": [],
            "completed": []
        }

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)