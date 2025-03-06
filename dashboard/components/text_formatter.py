import flet as ft
import re

class TextFormater:
    
    def get_selection(self):
        # Get current text, selection start and end positions
        text = self.description_field.value or ""
        selection_start = self.description_field.selection_start if self.description_field.selection else 0
        selection_end = self.description_field.selection_end if self.description_field.selection else 0
        
        # If no selection, use cursor position
        if selection_start == selection_end:
            return text, selection_start, selection_end, ""
        
        # Get selected text
        selected_text = text[selection_start:selection_end]
        return text, selection_start, selection_end, selected_text
    
    def update_text(self, new_text, new_selection_start=None, new_selection_end=None):
    
        self.description_field.value = new_text
        
        # Update selection if provided
        if new_selection_start is not None and new_selection_end is not None:
            self.description_field.selection = ft.TextSelection(
                start=new_selection_start,
                end=new_selection_end
            )
        
        # Trigger description update
        self.edit_description(None)
        self.description_field.update()
    
    def format_bold(self, e):
        """Apply bold formatting to selected text"""
        text, start, end, selected = self.get_selection()
        
        if not selected:
            # If no selection, insert bold markers at cursor position
            new_text = f"{text[:start]}**bold text**{text[end:]}"
            self.update_text(new_text, start + 2, start + 11)
        else:
            # Apply bold formatting to selected text
            new_text = f"{text[:start]}**{selected}**{text[end:]}"
            self.update_text(new_text, start, end + 4)
    
    def format_italic(self, e):
        """Apply italic formatting to selected text"""
        text, start, end, selected = self.get_selection()
        
        if not selected:
            # If no selection, insert italic markers at cursor position
            new_text = f"{text[:start]}*italic text*{text[end:]}"
            self.update_text(new_text, start + 1, start + 12)
        else:
            # Apply italic formatting to selected text
            new_text = f"{text[:start]}*{selected}*{text[end:]}"
            self.update_text(new_text, start, end + 2)
    
    def format_underline(self, e):
        """Apply underline formatting to selected text"""
        text, start, end, selected = self.get_selection()
        
        if not selected:
            # If no selection, insert underline markers at cursor position
            new_text = f"{text[:start]}__underlined text__{text[end:]}"
            self.update_text(new_text, start + 2, start + 17)
        else:
            # Apply underline formatting to selected text
            new_text = f"{text[:start]}__{selected}__{text[end:]}"
            self.update_text(new_text, start, end + 4)
    
    def format_strikethrough(self, e):
        """Apply strikethrough formatting to selected text"""
        text, start, end, selected = self.get_selection()
        
        if not selected:
            # If no selection, insert strikethrough markers at cursor position
            new_text = f"{text[:start]}~~strikethrough text~~{text[end:]}"
            self.update_text(new_text, start + 2, start + 20)
        else:
            # Apply strikethrough formatting to selected text
            new_text = f"{text[:start]}~~{selected}~~{text[end:]}"
            self.update_text(new_text, start, end + 4)
    
    def format_quote(self, e):
        """Format selected text as a quote"""
        text, start, end, selected = self.get_selection()
        
        # Find the beginning of the current line
        line_start = text.rfind("\n", 0, start) + 1
        if line_start == 0:  # If we're on the first line
            line_start = 0
            
        # If there's no selection, apply to the current line
        if not selected:
            current_line = text[line_start:text.find("\n", start) if text.find("\n", start) != -1 else len(text)]
            if current_line.startswith("> "):
                # Remove quote formatting
                new_text = f"{text[:line_start]}{current_line[2:]}{text[line_start + len(current_line):]}"
                self.update_text(new_text, line_start, line_start + len(current_line) - 2)
            else:
                # Add quote formatting
                new_text = f"{text[:line_start]}> {current_line}{text[line_start + len(current_line):]}"
                self.update_text(new_text, line_start + 2, line_start + len(current_line) + 2)
        else:
            # For multi-line selections, add quote to each line
            lines = selected.split("\n")
            quoted_lines = []
            for line in lines:
                if line.startswith("> "):
                    quoted_lines.append(line)  # Keep already quoted lines as is
                else:
                    quoted_lines.append(f"> {line}")
            quoted_text = "\n".join(quoted_lines)
            
            new_text = f"{text[:start]}{quoted_text}{text[end:]}"
            self.update_text(new_text, start, start + len(quoted_text))
    
    def format_code(self, e):
        """Format selected text as a code block"""
        text, start, end, selected = self.get_selection()
        
        if not selected:
            # If no selection, insert code block markers at cursor position
            new_text = f"{text[:start]}```\ncode block\n```{text[end:]}"
            self.update_text(new_text, start + 4, start + 14)
        else:
            # Check if already in a code block
            if selected.startswith("```") and selected.endswith("```"):
                # Remove code formatting
                content = selected[3:-3].strip()
                new_text = f"{text[:start]}{content}{text[end:]}"
                self.update_text(new_text, start, start + len(content))
            else:
                # Apply code block formatting
                new_text = f"{text[:start]}```\n{selected}\n```{text[end:]}"
                self.update_text(new_text, start, end + 8)
    
    def format_bullet_list(self, e):
        """Create or convert text to a bulleted list"""
        text, start, end, selected = self.get_selection()
        
        # Find the beginning of the current line
        line_start = text.rfind("\n", 0, start) + 1
        if line_start == 0:  # If we're on the first line
            line_start = 0
            
        # If there's no selection, apply to the current line
        if not selected:
            current_line = text[line_start:text.find("\n", start) if text.find("\n", start) != -1 else len(text)]
            if current_line.startswith("- "):
                # Remove bullet formatting
                new_text = f"{text[:line_start]}{current_line[2:]}{text[line_start + len(current_line):]}"
                self.update_text(new_text, line_start, line_start + len(current_line) - 2)
            else:
                # Add bullet formatting
                new_text = f"{text[:line_start]}- {current_line}{text[line_start + len(current_line):]}"
                self.update_text(new_text, line_start + 2, line_start + len(current_line) + 2)
        else:
            # For multi-line selections, add bullet to each line
            lines = selected.split("\n")
            bulleted_lines = []
            for line in lines:
                if not line.strip():  # Skip empty lines
                    bulleted_lines.append(line)
                    continue
                    
                if line.startswith("- "):
                    bulleted_lines.append(line)  # Keep already bulleted lines as is
                else:
                    bulleted_lines.append(f"- {line}")
            bulleted_text = "\n".join(bulleted_lines)
            
            new_text = f"{text[:start]}{bulleted_text}{text[end:]}"
            self.update_text(new_text, start, start + len(bulleted_text))
    
    def format_numbered_list(self, e):
        """Create or convert text to a numbered list"""
        text, start, end, selected = self.get_selection()
        
        # Find the beginning of the current line
        line_start = text.rfind("\n", 0, start) + 1
        if line_start == 0:  # If we're on the first line
            line_start = 0
            
        # Regular expression to match numbered list items (e.g., "1. ")
        numbered_pattern = re.compile(r'^\d+\.\s')
            
        # If there's no selection, apply to the current line
        if not selected:
            current_line = text[line_start:text.find("\n", start) if text.find("\n", start) != -1 else len(text)]
            if numbered_pattern.match(current_line):
                # Remove numbering
                match = numbered_pattern.match(current_line)
                prefix_len = match.end()
                new_text = f"{text[:line_start]}{current_line[prefix_len:]}{text[line_start + len(current_line):]}"
                self.update_text(new_text, line_start, line_start + len(current_line) - prefix_len)
            else:
                # Add numbering (1.)
                new_text = f"{text[:line_start]}1. {current_line}{text[line_start + len(current_line):]}"
                self.update_text(new_text, line_start + 3, line_start + len(current_line) + 3)
        else:
            # For multi-line selections, add numbering to each line
            lines = selected.split("\n")
            numbered_lines = []
            
            for i, line in enumerate(lines, 1):
                if not line.strip():  # Skip empty lines
                    numbered_lines.append(line)
                    continue
                    
                if numbered_pattern.match(line):
                    # Keep existing numbered format but update the number
                    new_line = numbered_pattern.sub(f"{i}. ", line)
                    numbered_lines.append(new_line)
                else:
                    numbered_lines.append(f"{i}. {line}")
                    
            numbered_text = "\n".join(numbered_lines)
            
            new_text = f"{text[:start]}{numbered_text}{text[end:]}"
            self.update_text(new_text, start, start + len(numbered_text))
    
    def format_checklist(self, e):
        """Create or convert text to a checklist"""
        text, start, end, selected = self.get_selection()
        
        # Find the beginning of the current line
        line_start = text.rfind("\n", 0, start) + 1
        if line_start == 0:  # If we're on the first line
            line_start = 0
            
        # Regular expression to match checklist items (e.g., "- [ ] " or "- [x] ")
        checklist_pattern = re.compile(r'^- \[([ xX])\]\s')
            
        # If there's no selection, apply to the current line
        if not selected:
            current_line = text[line_start:text.find("\n", start) if text.find("\n", start) != -1 else len(text)]
            if checklist_pattern.match(current_line):
                # Remove checklist formatting
                match = checklist_pattern.match(current_line)
                prefix_len = match.end()
                new_text = f"{text[:line_start]}{current_line[prefix_len:]}{text[line_start + len(current_line):]}"
                self.update_text(new_text, line_start, line_start + len(current_line) - prefix_len)
            else:
                # Add checklist formatting (unchecked)
                new_text = f"{text[:line_start]}- [ ] {current_line}{text[line_start + len(current_line):]}"
                self.update_text(new_text, line_start + 6, line_start + len(current_line) + 6)
        else:
            # For multi-line selections, add checklist to each line
            lines = selected.split("\n")
            checklist_lines = []
            
            for line in lines:
                if not line.strip():  # Skip empty lines
                    checklist_lines.append(line)
                    continue
                    
                if checklist_pattern.match(line):
                    # Keep already formatted checklist lines as is
                    checklist_lines.append(line)
                else:
                    checklist_lines.append(f"- [ ] {line}")
                    
            checklist_text = "\n".join(checklist_lines)
            
            new_text = f"{text[:start]}{checklist_text}{text[end:]}"
            self.update_text(new_text, start, start + len(checklist_text))
    
    def apply_heading_style(self, e):
        """Apply heading style based on dropdown selection"""
        if not self.description_field.value:
            return
            
        text, start, end, selected = self.get_selection()
        
        # Find the beginning of the current line
        line_start = text.rfind("\n", 0, start) + 1
        if line_start == 0:  # If we're on the first line
            line_start = 0
            
        # Get the current line
        current_line = text[line_start:text.find("\n", start) if text.find("\n", start) != -1 else len(text)]
        
        # Remove any existing heading markers
        clean_line = re.sub(r'^#{1,6}\s', '', current_line)
        
        # Apply new heading style
        if e.control.value == "Heading 1":
            new_line = f"# {clean_line}"
        elif e.control.value == "Heading 2":
            new_line = f"## {clean_line}"
        elif e.control.value == "Heading 3":
            new_line = f"### {clean_line}"
        else:  # Normal
            new_line = clean_line
            
        # Update text
        new_text = f"{text[:line_start]}{new_line}{text[line_start + len(current_line):]}"
        self.update_text(new_text, line_start, line_start + len(new_line))