# Given an array (arr) as an argument complete the function countSmileys
# that should return the total number of smiling faces.
#
# Rules for a smiling face:
#
# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.
#
# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]

# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

def countSmileys(faces):
    eyes = [":", ";"]
    nose = ["-", "~"]
    smile = [")", "D"]
    counter = 0
    for face in faces:
        if len(face)==3:
            face=[i for i in face]
            if face[0] in eyes and face[1] in nose and face[2] in smile:
                counter += 1
        elif len(face)==2:
            if face[0] in eyes and face[1] in smile:
                counter += 1
    return counter


# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

print(countSmileys([';]', ':[', ';*', ':$', ';-D']))