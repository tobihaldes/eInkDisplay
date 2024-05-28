from tiles import Tile
import framebuf


class Template_Tile(Tile):
    
    width = 240
    height = 240
    
    red = 0xff
    black = 0x00
    
    def draw_canvas(self, can):
        can.imagered.ellipse(self.x+200, self.y+10, 100, 100, red, True)
        
        y_row_counter = 0
        row_count = 0
        max_rows = 10
        cols = 200 // 8 #Breite des Textfeldes
        current_row = ''
        last_space_index = -1  
        text = "Das ist ein langer Text der in jedem Fall einen Zeilenumbruch benötigen wird. Das lässt sich nicht verhindern ab einer bestimmten Länge. Vor allem wenn jetzt noch ein Satz kommt wird es echt kritisch. Mit jedem Wort wird es schlimmer und schlimmer und schlimmer... Ich sollte jetzt einfach aufhören!"+" "
        
        for i in range(len(text)):
            current_row += text[i]
            if text[i] == ' ':
                last_space_index = i  
            if len(current_row) == cols or (i == len(text) - 1):  # Wenn die maximale Spaltenbreite erreicht ist.
                # Zeichne die aktuelle Zeile bis zum letzten Leerzeichen
                can.imageblack.text(current_row[:last_space_index], self.x+10, self.y+10 + y_row_counter, black)
                # Entferne den Teil, der bereits gezeichnet wurde, aus dem aktuellen Text
                current_row = current_row[last_space_index + 1:]
                y_row_counter += 8  # Zeilenhöhe
                row_count += 1
                last_space_index = -1 
                if row_count >= max_rows:
                    break
        # Zeichne den Rest der letzten Zeile, wenn sie nicht vollständig war
        if current_row:
            can.imageblack.text(current_row, self.x+10, self.y+10 + y_row_counter, black)
        
        