from PyQt4 import QtGui, QtCore

class Window(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self._offset = 200
        self._closed = False
        self._maxwidth = self.maximumWidth()
        self.editor = QtGui.QTextEdit(self)
        self.editor.setMaximumWidth(self._offset)
        self.button = QtGui.QPushButton("Do",self)
        layout = QtGui.QHBoxLayout(self)
        # layout.addWidget(self.widget)
       
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.work())

        self.string ="Girish ramnani is my name "
        layout.addWidget(self.editor)
        layout.addWidget(self.button)
        self.button.clicked.connect(lambda : self.timer.start(100))
    def work(self):
        def word_animate():
            
            if word_animate.i <len(self.string):
                self.editor.moveCursor(QtGui.QTextCursor.End)
                self.editor.insertPlainText(self.string[word_animate.i])
                self.editor.moveCursor(QtGui.QTextCursor.End)
                word_animate.i+=1
            else:
                self.timer.stop()
        word_animate.i=0
        return word_animate
    

        
if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.move(500, 300)
    window.show()
    sys.exit(app.exec_())