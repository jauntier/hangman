import random

def choose_word():
    words_string = """abruptly
    absurd
    abyss
    affix
    askew
    avenue
    awkward
    axiom
    azure
    bagpipes
    bandwagon
    banjo
    bayou
    beekeeper
    bikini
    blitz
    blizzard
    boggle
    bookworm
    boxcar
    boxful
    buckaroo
    buffalo
    buffoon
    buxom
    buzzard
    buzzing
    buzzwords
    caliph
    cobweb
    cockiness
    croquet
    crypt
    curacao
    cycle
    daiquiri
    dirndl
    disavow
    dizzying
    duplex
    dwarves
    embezzle
    equip
    espionage
    euouae
    exodus
    faking
    fishhook
    fixable
    fjord
    flapjack
    flopping
    fluffiness
    flyby
    foxglove
    frazzled
    frizzled
    fuchsia
    funny
    gabby
    galaxy
    galvanize
    gazebo
    giaour
    gizmo
    glowworm
    glyph
    gnarly
    gnostic
    gossip
    grogginess
    haiku
    haphazard
    hyphen
    iatrogenic
    icebox
    injury
    ivory
    ivy
    jackpot
    jaundice
    jawbreaker
    jaywalk
    jazziest
    jazzy
    jelly
    jigsaw
    jinx
    jiujitsu
    jockey
    jogging
    joking
    jovial
    joyful
    juicy
    jukebox
    jumbo
    kayak
    kazoo
    keyhole
    khaki
    kilobyte
    kiosk
    kitsch
    kiwifruit
    klutz
    knapsack
    larynx
    lengths
    lucky
    luxury
    lymph
    marquis
    matrix
    megahertz
    microwave
    mnemonic
    mystify
    naphtha
    nightclub
    nowadays
    numbskull
    nymph
    onyx
    ovary
    oxidize
    oxygen
    pajama
    peekaboo
    phlegm
    pixel
    pizazz
    pneumonia
    polka
    pshaw
    psyche
    puppy
    puzzling
    quartz
    queue
    quips
    quixotic
    quiz
    quizzes
    quorum
    razzmatazz
    rhubarb
    rhythm
    rickshaw
    schnapps
    scratch
    shiv
    snazzy
    sphinx
    spritz
    squawk
    staff
    strength
    strengths
    stretch
    stronghold
    stymied"""


    words = words_string.split("\n")



    
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    while attempts > 0:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You won. The word was '{word}'.")
            break

    if attempts == 0:
        print(f"Out of attempts! The word was '{word}'. You lost.")

hangman()