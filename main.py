# main.py - TekAI için Kivy arayüzü (APK giriş dosyası)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import tek_ai

class TekAIApp(App):
    def build(self):
        self.ai = tek_ai.TekAI()
        layout = BoxLayout(orientation='vertical')
        
        self.output = Label(text='TekAI Hazır', size_hint_y=2, halign='center', valign='middle')
        self.output.bind(size=self.output.setter('text_size'))
        
        self.input = TextInput(text='', multiline=False, size_hint_y=0.5)
        self.input.bind(on_text_validate=self.gonder)
        
        gonder_btn = Button(text='Gönder', size_hint_y=0.5)
        gonder_btn.bind(on_press=self.gonder)
        
        layout.add_widget(self.output)
        layout.add_widget(self.input)
        layout.add_widget(gonder_btn)
        
        return layout
    
    def gonder(self, instance):
        mesaj = self.input.text.strip()
        if not mesaj:
            return
        if mesaj.lower() in ['çık', 'exit', 'kapat']:
            App.get_running_app().stop()
            return
        cevap = self.ai.cevapla(mesaj)
        self.output.text = f"Sen: {mesaj}\nTekAI: {cevap}"
        self.input.text = ''

if __name__ == '__main__':
    TekAIApp().run()
