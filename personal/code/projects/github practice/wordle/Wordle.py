import random

def randomWord():
    words = [
    "apple", "brave", "charm", "drift", "eager",
    "flint", "grasp", "haste", "ideal", "jolly",
    "knack", "latch", "mirth", "noble", "oasis",
    "pluck", "query", "roast", "scale", "truce",
    "ultra", "vivid", "waste", "xenon", "yearn",
    "zebra", "quake", "gloom", "frost", "sweep",
    "bloom", "blush", "creep", "dwarf", "flame",
    "glide", "grief", "pride", "sloth", "smile",
    "snarl", "spark", "spill", "squat", "stack",
    "steal", "sting", "stoop", "swell", "swoop"]
    
    return random.choice(words)

print(randomWord())