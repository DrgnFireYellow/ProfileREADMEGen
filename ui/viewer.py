import json

#from rich.layout import Layout
from rich.panel import Panel
from textual import events
from textual.app import App
from textual.widget import Widget
from textual.widgets import Footer, Header


class certificationviewer(Widget):
    def render(self) -> Panel:
        data = json.load("data/certifications.json")
        for key in data:
            
        return Panel()

class ProfileReadmeGenViewer(App):
    async def on_load(self, events: events.Load) -> None:
        await self.bind("q", "quit", "Quit")
    async def on_mount(self, events: events.Mount) -> None :
        await self.view.dock(Footer(), edge="bottom")
        await self.view.dock(Header(), edge="top")
ProfileReadmeGenViewer.run(title="ProfileREADMEGen Data Viewer")
