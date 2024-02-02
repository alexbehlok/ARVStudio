from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

# Placeholder for the image pool and events storage
image_pool = ['image1.jpg', 'image2.jpg', 'image3.jpg']  # Add your images here
events = {}

@app.route('/setup')
def setup_tab():
    # Placeholder for setup tab functionality
    return "Setup tab content"

@app.route('/tasking')
def tasking_tab():
    # Placeholder for tasking tab functionality
    return "Tasking tab content"

@app.route('/judging')
def judging_tab():
    # Placeholder for judging tab functionality
    return "Judging tab content"

@app.route('/setup', methods=['POST'])
def setup_event():
    data = request.json
    event_number = data.get('event_number')
    trn_type = data.get('trn_type')
    photo_target_pair_mode = data.get('photo_target_pair_mode')
    # Store the event setup details
    events[event_number] = {
        'trn_type': trn_type,
        'photo_target_pair_mode': photo_target_pair_mode,
        'tasking': None,
        'judging': None
    }
    return jsonify({'message': 'Event setup complete', 'event_number': event_number})

@app.route('/tasking', methods=['POST'])
def task_event():
    data = request.json
    event_number = data.get('event_number')
    event_info = {
        'event_date': data.get('event_date'),
        'event_time': data.get('event_time'),
        'event_timezone': data.get('event_timezone', 'EST'),
        'event_type': data.get('event_type'),
        'event_pair': data.get('event_pair'),
        'outcomes': data.get('outcomes'),
        'full_line_info': data.get('full_line_info'),
    }
    # Generate TRN and assign images
    trn = ''.join(random.choices(string.digits, k=events[event_number]['trn_type']))
    assigned_images = random.sample(image_pool, 2)
    image_outcome_pairs = {
        trn: {
            'image1': {'outcome1': assigned_images[0], 'outcome2': assigned_images[1]},
            'image2': {'outcome1': assigned_images[1], 'outcome2': assigned_images[0]}
        }
    }
    events[event_number]['tasking'] = {
        'event_info': event_info,
        'image_outcome_pairs': image_outcome_pairs
    }
    return jsonify({'message': 'Tasking complete', 'event_number': event_number, 'trn': trn})

if __name__ == '__main__':
    app.run(debug=True)
