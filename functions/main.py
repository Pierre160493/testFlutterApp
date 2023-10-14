# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

import random
from firebase_functions import firestore_fn, https_fn
from firebase_admin import initialize_app, firestore
import google.cloud.firestore

# initialize_app()
app = initialize_app()

# @https_fn.on_request()
# def on_request_example(req: https_fn.Request) -> https_fn.Response:
#     return https_fn.Response("Hello world!")

@https_fn.on_request()
def addmessage(req: https_fn.Request) -> https_fn.Response:
    """Take the text parameter passed to this HTTP endpoint and insert it into
    a new document in the messages collection."""
    # Grab the text parameter.
    original = req.args.get("text")
    if original is None:
        return https_fn.Response("No text parameter provided", status=400)

    firestore_client: google.cloud.firestore.Client = firestore.client()

    # Push the new message into Cloud Firestore using the Firebase Admin SDK.
    _, doc_ref = firestore_client.collection("messages").add(
        {"original": original}
    )

    # Send back a message that we've successfully written the message
    return https_fn.Response(f"Message with ID {doc_ref.id} added.")

@firestore_fn.on_document_created(document="messages/{pushId}")
def makeuppercase(
    event: firestore_fn.Event[firestore_fn.DocumentSnapshot | None],
) -> None:
    """Listens for new documents to be added to /messages. If the document has
    an "original" field, creates an "uppercase" field containing the contents of
    "original" in upper case."""

    # Get the value of "original" if it exists.
    if event.data is None:
        return
    try:
        original = event.data.get("original")
    except KeyError:
        return # No "original" field, so do nothing.

    # Set the "uppercase" field.
    print(f"Uppercasing {event.params['pushId']}: {original}")
    upper = original.upper()
    event.data.reference.update({"uppercase": upper})


############################################################################################################
############################################################################################################
############ Add First Name and Last Name for generating player name
@https_fn.on_request()
def add_to_name_generator(req: https_fn.Request) -> https_fn.Response:
    """Add first names and last names in the player_name_generator collection
    Mandatory: Type of add (Players, ...); Country
    Optional: FirstName; LastName; Position
    http://localhost:5001/openhattrick/us-central1/add_to_player_name_generator/?Country=France&FirstName=Pierre&LastName=Granger&Position=CB
    """

    #FieldTypeOfAdd="TypeOfAdd"
    FieldCountry="Country"
    FieldFirstName="FirstName"
    FieldLastName="LastName"
    FieldPosition="Position"

    strDocument1 = "Players"
    #if strDocument is None:
    #    return https_fn.Response(f"Oups... {FieldTypeOfAdd} parameter is mandatory, we found nothing as input ==> Must be Players", status=400)

    strCountry = req.args.get(FieldCountry)
    if strCountry is None:
        return https_fn.Response(f"Oups... {FieldCountry} parameter is mandatory, we found nothing as input", status=400)

    FirstName = req.args.get(FieldFirstName)
    LastName = req.args.get(FieldLastName)
    if FirstName is None and LastName is None:
        return https_fn.Response(f"You must at least specify a {FieldFirstName} or a {FieldLastName} ==> Found none for both !", status=400)

    db: google.cloud.firestore.Client = firestore.client()
    strCollection1 = "NameGenerator"
    strCollection2 = strCountry
    strPath = f"[{strCollection1}/{strDocument1}/{strCollection2}]" #Path of the document we want to create

    #try:
    #    doc_ref = db.collection(strCollection1).document(strDocument1).collection(strCollection2)
    #    doc = doc_ref.get()
    #    if not doc.exists:
    #        return https_fn.Response(f"The path: {strPath} is unknown", status=400)
    #except Exception as e:
    #    print(f"An error occurred: {e}")
    #    return https_fn.Response(f"Error when opening the path: {strPath} ==> {e}", status=400)

    strAdd = None
    if FirstName is not None: # Push the new FirstName in the db
        strAdd = {
            FieldFirstName: FirstName,
        }

    if LastName is not None: # Push the new LastName in the db
        strAdd.update({FieldLastName: LastName})

        Position = req.args.get(FieldPosition)
        if Position is not None:
            strAdd .update({FieldPosition: Position})

    _, doc_ref = db.collection(strCollection1).document(strDocument1).collection(strCollection2).add(strAdd)


    # Send back a message that we've successfully written the message
    return https_fn.Response(f"Successfully added new document [{strAdd}] in the path {strPath}")

############################################################################################################
############################################################################################################
############ Create Player
@https_fn.on_request()
def createPlayer(req: https_fn.Request) -> https_fn.Response:
    """Player creation
    Mandatory: age
    Optional: club_id, name, surname
    """
    age = req.args.get("age")
    if age is None:
        return https_fn.Response("Oups... age parameter is mandatory, we found nothing", status=400)
    try: #try cast as float
        float(age)
        #float(age.str.replace(',','.')) #Transform comma with dot (Vive la France !)
    except ValueError:
        return https_fn.Response(f"Oups... age parameter cannot be cast as a number ==> input was [{age}]", status=400)
    age = float(age)
    if age < 15 or age >= 100:
        return https_fn.Response(f"age must be between 15 and 99 ==> Input was {age}", status=400)
    club_id = req.args.get("club_id")
    if club_id is None:
        club_id = 0 #Then the player doesn't have any club
    FirstName = req.args.get("FirstName")
    if FirstName is None:
        FirstName = "testFirstName"
    LastName = req.args.get("LastName")
    if LastName is None:
        LastName = "testLastName"


    firestore_client: google.cloud.firestore.Client = firestore.client()

    # Push the new message into Cloud Firestore using the Firebase Admin SDK.
    _, doc_ref = firestore_client.collection("Players").add(
        {
            "FirstName": FirstName,
            "LastName": LastName,
            "douAge": age,
            "club_id": club_id,
            "DateCreation": firestore.SERVER_TIMESTAMP
        }
    )

    # Send back a message that we've successfully written the message
    return https_fn.Response(f"Successfully created [{FirstName} {LastName.uppercase()}] with id {doc_ref.id}.")


############################################################################################################
############################################################################################################
############ Create Club
@https_fn.on_request()
def createClub(req: https_fn.Request) -> https_fn.Response:
    """Club creation
    Mandatory: Country
    Optional: NameClub

    http://127.0.0.1:5001/openhattrick/us-central1/createClub/?Country=France&NameClub=FC%20Bordeaux
    """

    firestore_client: google.cloud.firestore.Client = firestore.client()

###### Country
    Country = req.args.get("Country")
    if Country is None:
        return https_fn.Response("Oups... Country parameter is mandatory, we found nothing", status=400)
    elif Country not in ["France", "Test"]:
        return https_fn.Response(f"Oups... Country [{Country}] doesn't exist yet", status=400)
    strDocument1 = Country

###### Name
    NameClub = req.args.get("NameClub")
    if NameClub is None:
        FieldCity = "City"
        strCollection1 = "NameGenerator"
        strCollection2 = "Clubs"
        doc_ref = firestore_client.collection(strCollection1).document(strDocument1).collection(strCollection2)
        docs = doc_ref.get()
        n_docs = len([doc for doc in docs])
        # return https_fn.Response(f"Oups... n_docs [{n_docs}] doesn't exist yet", status=400)
        while NameClub is None:
            random_index = random.randint(0, n_docs - 1)
            # Query and retrieve the random document
            # rand_doc = doc_ref.limit(1).offset(random_index).get()
            rand_doc = docs[random_index]
            
            if rand_doc.exists:
                # return https_fn.Response(f"Oups... n_docs [{random_index}] doesn't exist yet", status=400)
                data = rand_doc.to_dict()
                # return https_fn.Response(f"Oups... n_docs [{random_index}] doesn't exist yet", status=400)
                if FieldCity in data:
                    # Field exists in the document
                    NameClub = data[FieldCity]
                else:
                    return https_fn.Response(f"1Oups... n_docs [{random_index}] doesn't exist yet", status=400)
            else:
                return https_fn.Response(f"2Oups... n_docs [{random_index}] doesn't exist yet", status=400)
        NameClub = random.choice(["FC", "FC", "AS", "Union", "Entente"]) + f" {NameClub}"


    # return https_fn.Response(f"Oups... n_docs [{NameClub}] doesn't exist yet", status=400)
    
###### Stadium
    NameStadium = req.args.get("NameStadium")
    if NameStadium is None:
        NameStadium = random.choice(["Stade de la Mairie", "Stade de l'école"])

    # Push the new Club into Cloud Firestore using the Firebase Admin SDK.
    _, doc_ref = firestore_client.collection("Clubs").add(
        {
            "Country": Country,
            "Name": NameClub,
            "TeamSpirit": 60,
            "TeamConfidence": 60,
            "Money": 250000,
            "Stadium": {
                "Name": NameStadium,
                "Seats": {
                    "Uncovered": 1000,
                    "Covered": 500,
                    "VIP": 50
                }
            },
            "Fans": {
                "Mood": 60,
                "Number": 100
            },
            "DateCreation": firestore.SERVER_TIMESTAMP
        }
    )



    # Send back a message that we've successfully written the message
    return https_fn.Response(f"Successfully created [{NameClub}] with id {doc_ref.id}.")