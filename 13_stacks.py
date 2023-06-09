# stack lifo (last in first out)
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print("list of session on browser", browsing_session)
last = browsing_session.pop()
print("last session on browser", last)
print("current browsing session on browser", browsing_session)
# we use -1 to redirect to previous session of the stack
if not browsing_session:
    print("redirect", browsing_session[-1])
