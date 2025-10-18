SHAPE = {
'arrow': 'curve -d 1 -p -1 0 1 -p -1 0 3 -p -2 0 3 -p 0 0 5 -p 2 0 3 -p 1 0 3 -p 1 0 1 -p 3 0 1 -p 3 0 2 -p 5 0 0 -p 3 0 -2 -p 3 0 -1 -p 1 0 -1 -p 1 0 -3 -p 2 0 -3 -p 0 0 -5 -p -2 0 -3 -p -1 0 -3 -p -1 0 -1 -p -3 0 -1 -p -3 0 -2 -p -5 0 0 -p -3 0 2 -p -3 0 1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 ',
'circle3d': 'curve -d 1 -p 1 0 0 -p 0.707107 0.707107 0 -p 0 1 0 -p -0.707107 0.707107 0 -p -1 0 0 -p -0.707107 -0.707107 0 -p 0 -1 0 -p 0.707107 -0.707107 0 -p 1 0 0 -p 0.707107 0 -0.707107 -p 0 0 -1 -p -0.707107 0 -0.707107 -p -1 0 0 -p -0.707107 0 0.707107 -p 0 0 1 -p 0.707107 0 0.707107 -p 1 0 0 -p 0.707107 0 -0.707107 -p 0 0 -1 -p 0 0.707107 -0.707107 -p 0 1 0 -p 0 0.707107 0.707107 -p 0 0 1 -p 0 -0.707107 0.707107 -p 0 -1 0 -p 0 -0.707107 -0.707107 -p 0 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 ;',
'cube3d': 'curve -d 1 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 ;',
'star3d' : 'curve -d 1 -p 0 1 0 -p 0 -1 0 -p 0 0 0 -p -1 0 0 -p 1 0 0 -p 0 0 0 -p 0 0 1 -p 0 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;',
'up' : 'curve -d 1 -p -1 0 -1 -p -1 0 3 -p 1 0 3 -p 1 0 -1 -p 2 0 -1 -p 0 0 -3 -p -2 0 -1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;',
'circle' : 'circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.0001 -s 8 -ch 0;',
'plus' : 'curve -d 1 -p -1 0 -1 -p -1 0 -4 -p 1 0 -4 -p 1 0 -1 -p 4 0 -1 -p 4 0 1 -p 1 0 1 -p 1 0 4 -p -1 0 4 -p -1 0 1 -p -4 0 1 -p -4 0 -1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 ;',
'diamond' : 'curve -d 1 -p -2 0 -2 -p 2 0 -2 -p 3 0 -1 -p 0 0 2 -p -3 0 -1 -p -2 0 -2 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 ;',
'triangle' : 'curve -d 1 -p 0 0 -1 -p -1 0 1 -p 1 0 1 -p 0 0 -1 -k 0 -k 1 -k 2 -k 3 ;',
'triangle3d' : 'curve -d 1 -p 0 1 0 -p -0.707107 -1 -0.707107 -p 0.707107 -1 -0.707107 -p 0 1 0 -p 0.707107 -1 0.707107 -p 0.707107 -1 -0.707107 -p 0.707107 -1 0.707107 -p 0 1 0 -p -0.707107 -1 0.707107 -p 0.707107 -1 0.707107 -p -0.707107 -1 0.707107 -p 0 1 0 -p -0.707107 -1 -0.707107 -p -0.707107 -1 0.707107 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 ;',
'cube' : 'curve -d 1 -p 1 0 1 -p 1 0 -1 -p -1 0 -1 -p -1 0 1 -p 1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 ;',
'gear' : 'curve -d 1 -p -0.61075 0.5 -0.77629 -p -0.483474 0.5 -0.861333 -p -0.510928 0.5 -0.9582 -p -0.505939 0.5 -1.068506 -p -0.397795 0.5 -1.113301 -p -0.316269 0.5 -1.038831 -p -0.267186 0.5 -0.950922 -p -0.117054 0.5 -0.980785 -p -0.105349 0.5 -1.080785 -p -0.0585271 0.5 -1.180785 -p 0.058527 0.5 -1.180785 -p 0.105349 0.5 -1.080785 -p 0.117054 0.5 -0.980785 -p 0.267186 0.5 -0.950922 -p 0.316269 0.5 -1.038831 -p 0.397795 0.5 -1.113301 -p 0.505939 0.5 -1.068506 -p 0.510928 0.5 -0.9582 -p 0.483474 0.5 -0.861333 -p 0.61075 0.5 -0.77629 -p 0.689738 0.5 -0.838724 -p 0.793556 0.5 -0.876326 -p 0.876326 0.5 -0.793556 -p 0.838723 0.5 -0.689738 -p 0.77629 0.5 -0.61075 -p 0.861333 0.5 -0.483474 -p 0.9582 0.5 -0.510928 -p 1.068506 0.5 -0.505939 -p 1.113301 0.5 -0.397795 -p 1.038831 0.5 -0.316269 -p 0.950922 0.5 -0.267186 -p 0.980785 0.5 -0.117054 -p 1.080785 0.5 -0.105349 -p 1.180785 0.5 -0.0585272 -p 1.180785 0.5 0.058527 -p 1.080785 0.5 0.105349 -p 0.980785 0.5 0.117054 -p 0.950922 0.5 0.267186 -p 1.038831 0.5 0.316269 -p 1.113301 0.5 0.397795 -p 1.068506 0.5 0.505939 -p 0.9582 0.5 0.510928 -p 0.861333 0.5 0.483474 -p 0.77629 0.5 0.61075 -p 0.838723 0.5 0.689738 -p 0.876326 0.5 0.793556 -p 0.793556 0.5 0.876326 -p 0.689738 0.5 0.838723 -p 0.61075 0.5 0.77629 -p 0.483474 0.5 0.861333 -p 0.510928 0.5 0.9582 -p 0.505939 0.5 1.068506 -p 0.397795 0.5 1.113301 -p 0.316269 0.5 1.038831 -p 0.267186 0.5 0.950922 -p 0.117054 0.5 0.980785 -p 0.105349 0.5 1.080785 -p 0.0585271 0.5 1.180785 -p -0.0585271 0.5 1.180785 -p -0.105349 0.5 1.080785 -p -0.117054 0.5 0.980785 -p -0.267186 0.5 0.950922 -p -0.316269 0.5 1.038831 -p -0.397795 0.5 1.113301 -p -0.505939 0.5 1.068506 -p -0.510928 0.5 0.9582 -p -0.483474 0.5 0.861333 -p -0.61075 0.5 0.77629 -p -0.689737 0.5 0.838724 -p -0.793556 0.5 0.876326 -p -0.876326 0.5 0.793557 -p -0.838723 0.5 0.689738 -p -0.77629 0.5 0.61075 -p -0.861333 0.5 0.483474 -p -0.9582 0.5 0.510928 -p -1.068506 0.5 0.505939 -p -1.113301 0.5 0.397795 -p -1.038831 0.5 0.316269 -p -0.950922 0.5 0.267186 -p -0.980785 0.5 0.117054 -p -1.080785 0.5 0.105349 -p -1.180785 0.5 0.0585272 -p -1.180785 0.5 -0.058527 -p -1.080785 0.5 -0.105349 -p -0.980785 0.5 -0.117054 -p -0.950922 0.5 -0.267186 -p -1.038831 0.5 -0.316269 -p -1.113301 0.5 -0.397795 -p -1.068506 0.5 -0.505939 -p -0.9582 0.5 -0.510928 -p -0.861333 0.5 -0.483474 -p -0.77629 0.5 -0.61075 -p -0.838724 0.5 -0.689737 -p -0.876326 0.5 -0.793556 -p -0.793556 0.5 -0.876326 -p -0.689738 0.5 -0.838723 -p -0.61075 0.5 -0.77629 -p -0.483474 0.5 -0.861333 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 -k 82 -k 83 -k 84 -k 85 -k 86 -k 87 -k 88 -k 89 -k 90 -k 91 -k 92 -k 93 -k 94 -k 95 -k 96 -k 97 ;'

}
SHAPE_NAME = [
	"circle3d","cube3d","star3d","triangle3d","arrow","circle","cube",
	"diamond","gear","plus","triangle","up"
]

SIDE = ["","left","right","mid"]
SUFFIX = ["CC","cc","CTRL","ctrl"]
PADDING = [1,2,3,4]
TYPE = ["Keyable","Displayable","Hidden"] 
GREENHOVERBUTTON = '''
				QPushButton {
					background-color : #col; 
					color : Black;
					border-radius : 1px;
					font-family : "Comic Sans MS", cursive;
					padding : 8px;
				}
				QPushButton:hover {
					background-color : #B9E3B6;
				}
				QPushButton:pressed {
					background-color : #D3F7D0;
				}
			'''
REDHOVERBUTTON = '''
				QPushButton {
					background-color : #col;
					color : Black;
					border-radius : 1px;
					font-family : "Comic Sans MS", cursive;
					padding : 8px;
				}
				QPushButton:hover {
					background-color : #D93E30;
				}
				QPushButton:pressed {
					background-color : #FFCAC4;
				}
				
			'''
CURVEHOVERBUTTON = '''
				QPushButton {
					background-color : #DEB68E;
					color : white;
					border-radius : 10px;
					font-size : 20px;
					padding : 8px;
					font-family : "Comic Sans MS", cursive;
					font-weight : bold;
				}
				QPushButton:hover {
					background-color : #629C7D;
				}
				QPushButton:pressed {
					background-color : #B1F0CF;
				}
			'''
ADDATTRHOVERBUTTON = '''
				QPushButton {
					background-color : #A67B58;
					color : white;
					border-radius : 10px;
					font-size : 20px;
					padding : 8px;
					font-family : "Comic Sans MS", cursive;
					font-weight : bold;
				}
				QPushButton:hover {
					background-color : #D4AD77;
				}
				QPushButton:pressed {
					background-color : #EDD3AF;
				}
				
			'''
CONNECTHOVERBUTTON = '''
				QPushButton {
					background-color : #5C3210;
					color : white;
					border-radius : 10px;
					font-size : 20px;
					padding : 8px;
					font-family : "Comic Sans MS", cursive;
					font-weight : bold;
				}
				QPushButton:hover {
					background-color : #A48DB5;
				}
				QPushButton:pressed {
					background-color : #DDC2F2;
				}
				
			'''
EXITHOVERBUTTON = '''
				QPushButton {
					background-color : #AB483A;
					color : white;
					border-radius : 10px;
					font-size : 20px;
					padding : 8px;
					font-family : "Comic Sans MS", cursive;
					font-weight : bold;
				}
				QPushButton:hover {
					background-color : #A16480;
				}
				QPushButton:pressed {
					background-color : #DE8EB4;
				}
			'''