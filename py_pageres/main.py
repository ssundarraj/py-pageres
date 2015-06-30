from ghost import Ghost
ghost = Ghost()
page, resources = ghost.open('http://google.com')
ghost.capture_to('header.png', selector="body")
