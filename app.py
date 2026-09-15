from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# HELPER FUNCTION: USED WHEN LOOKING UP EVENTS
def find_event(event_id):
    return next((event for event in events if event.id == event_id), None)


# CREATE A NEW EVENT FROM JSON INPUT
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    # validate that a title was provided
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
 
    # generate the next id (1 if the list is empty, otherwise max + 1)
    new_id = max((event.id for event in events), default=0) + 1
 
    new_event = Event(new_id, data["title"])
    events.append(new_event)
 
    return jsonify(new_event.to_dict()), 201


# UPDATE THE TITLE OF AN EXISTING EVENT
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = find_event(event_id)    # lookup the event by id
 
    if not event:
        return jsonify({"error": "Event not found"}), 404   # no matching event found
 
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400 # title missing
 
    event.title = data["title"]     # update the title in place
 
    return jsonify(event.to_dict()), 200    # return the updated file


# REMOVVE AN EVENT FROM THE LIST
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = find_event(event_id)  # look up the event by id

    if not event:
        return jsonify({"error": "Event not found"}), 404  # no matching event

    events.remove(event)  # remove it from the in-memory list

    return "", 204  # no content to return



if __name__ == "__main__":
    app.run(debug=True)
