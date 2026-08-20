# activity 1

student_id = {
"Id1" : {"name" : "Alice", "age" : '13', "subject" : "math"},
"Id2"  : {"name" : "Josh", "age" : "12", "subject" : "science"  },
"Id3" : {"name" : "Jesica", "age" : "13", "subject" : "art"},
"Id4" : {"name" : "Jesica", "age" : "13", "subject" : "art"},
}

results = {}
seen_list = []

for student_id, details in student_id.items():
    unique_key = (details ["name"], details["age"], details["subject"])
    if unique_key not in seen_list:
        seen_list.append(unique_key)
        results [student_id] = details
for k, v in results.items():
    print  (k, ":", v)