import sublime
import sublime_plugin


class AlternateselectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		(row,col) = self.view.rowcol(self.view.sel()[0].begin())
		#self.view.insert(edit, 0, "Hello, World!")
		print(row, col, self.view.size())

		vai = True
		while(vai):
			pt = self.view.text_point(row, 0)
			selectRegion = self.view.line(pt)
			self.view.sel().add(selectRegion)
			row += 2

			print(selectRegion.end())

			if selectRegion.end() >= self.view.size():
				vai = False
				

