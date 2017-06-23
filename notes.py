#  def myFunction(number):
# print(myArray[0, 2])


#    print(myArray)

#   for i in range(0, 3):
#      myArray[i, 2] = 1
# iLike = [4, 2]
#    #userLikes = np.movieData['user'].max
#    for id in iLike:
#        userLikes[id] = 1
#  print('id')
#    print(userLikes)
#    print("")
#    userLikes2 = myArray.sum(axis=1)
#    print(userLikes2)

#    print(userLikes.sum())

#    commonLikes = myArray * userLikes

#    jac = commonLikes.sum(axis=1)
#    print(jac)
#    print(jac.argmax())

#    list = (np.argwhere(myArray[1, :] == 1))
#    print(list.flatten())
print(movieData['user'].max)

myArray = np.zeros((4,5))
myArray[1,2] = 1


def myFunction(number):
    print(myArray[0,2])

print(myArray)

for i in range(0,3):
    myArray[i,2] = 1
iLike = [4, 2]
userLikes = np.movoeData['user'].max
for id in iLike:
    userLikes[id]= 1
    #  print('id')
print(userLikes)
print("")
userLikes2 = myArray.sum(axis=1)
print(userLikes2)

print(userLikes.sum())


commonLikes = myArray * userLikes

jac = commonLikes.sum(axis=1)
print(jac)
print(jac.argmax())

list = (np.argwhere(myArray[1, :] == 1))
print(list.flatten())





#  Print the max user
print(movieData['user'].max())

iLike = [4, 2]

#change into a 0/1 array
iLikeNp = np.zeros(5)

for i in iLike:
    iLikeNp[id] = 1

#how many likes does each user have
userLikesCount = userLikes.sum(axis = 1)
print(userLikes)
#how many items do iLike
print(iLike.sum())
#find the things we do in common
commonLikes = userLikes * iLikeNp
# how many things do we both like
userAnd = commonLikes.sum(axis=1)
print(userAnd)
#get the id of the max value in userAnd
print(userAnd.argmax())
# find all the movies under 1 like
list = np.argwhere(userLikes[1, :] == 1)
#the list is more readable if we flatten it
print(list.flatten())

for id in iLike:
    iLike[id] = 1

print(iLikeNp)

print(iLike * userInput)

andSum = iLike + userInput



