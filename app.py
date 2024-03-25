from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def cosmic_siren():
    """
    A cosmic endpoint that sings like a siren.
    Returns ethereal data or performs celestial tasks.
    """
    data_from_the_ether = {"message": "Greetings, wanderer of the stars!"}
    return data_from_the_ether
