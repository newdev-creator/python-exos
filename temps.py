### main.py
import tkinter as tk
from ui.interface import PlanificateurProduction

if __name__ == "__main__":
    root = tk.Tk()
    app = PlanificateurProduction(root)
    root.mainloop()


### ui/interface.py
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from core.dossiers import charger_donnees_test
from core.planning import generer_planning
from utils.export import exporter_json

class PlanificateurProduction:
    def __init__(self, root):
        self.root = root
        self.root.title("Planificateur de Production")
        self.root.geometry("1200x800")

        self.dossiers = []
        self.planning = []
        self.machines = ["M1", "M2"]
        self.equipes = {
            "Matin": {"debut": 6, "fin": 14, "operateurs": 1},
            "Apres-midi": {"debut": 14, "fin": 22, "operateurs": 2}
        }

        self.setup_ui()
        self.charger_donnees_test()

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(main_frame, text="Dossiers de Production", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=4, pady=10)

        self.tree_dossiers = ttk.Treeview(main_frame, columns=("quantite", "temps_unitaire", "temps_total", "livraison", "priorite"), show="headings", height=6)
        for col in self.tree_dossiers["columns"]:
            self.tree_dossiers.heading(col, text=col.replace("_", " ").capitalize())
            self.tree_dossiers.column(col, width=100)
        self.tree_dossiers.grid(row=1, column=0, columnspan=4, pady=10, sticky=(tk.W, tk.E))

        ttk.Button(main_frame, text="Ajouter Dossier", command=self.ajouter_dossier).grid(row=2, column=0, padx=5)
        ttk.Button(main_frame, text="Générer Planning", command=self.generer_planning).grid(row=2, column=1, padx=5)
        ttk.Button(main_frame, text="Exporter JSON", command=self.exporter_json).grid(row=2, column=2, padx=5)

        ttk.Separator(main_frame, orient="horizontal").grid(row=3, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=20)

        ttk.Label(main_frame, text="Planning Généré", font=("Arial", 12, "bold")).grid(row=4, column=0, columnspan=4, pady=10)

        self.tree_planning = ttk.Treeview(main_frame, columns=("date", "equipe", "machine", "dossier", "quantite", "debut", "fin", "mode"), show="headings", height=10)
        for col in self.tree_planning["columns"]:
            self.tree_planning.heading(col, text=col.capitalize())
            self.tree_planning.column(col, width=80)
        self.tree_planning.grid(row=5, column=0, columnspan=4, pady=10, sticky=(tk.W, tk.E))

        self.text_resume = tk.Text(main_frame, height=8, width=80)
        self.text_resume.grid(row=6, column=0, columnspan=4, pady=10, sticky=(tk.W, tk.E))

    def charger_donnees_test(self):
        self.dossiers = charger_donnees_test()
        self.actualiser_treeview_dossiers()

    def actualiser_treeview_dossiers(self):
        for item in self.tree_dossiers.get_children():
            self.tree_dossiers.delete(item)
        for i, dossier in enumerate(self.dossiers):
            temps_total = round(dossier["quantite"] * dossier["temps_unitaire"] / 60, 2)
            self.tree_dossiers.insert("", "end", iid=i, values=(
                dossier["quantite"], dossier["temps_unitaire"], temps_total, dossier["livraison"], dossier["priorite"]
            ))

    def ajouter_dossier(self):
        def valider():
            try:
                nouveau_dossier = {
                    "nom": f"Dossier {len(self.dossiers) + 1}",
                    "quantite": int(entry_quantite.get()),
                    "temps_unitaire": int(entry_temps.get()),
                    "livraison": entry_livraison.get(),
                    "priorite": int(entry_priorite.get())
                }
                self.dossiers.append(nouveau_dossier)
                self.actualiser_treeview_dossiers()
                fenetre.destroy()
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des valeurs valides")

        fenetre = tk.Toplevel(self.root)
        fenetre.title("Ajouter un Dossier")
        fenetre.geometry("300x200")

        for i, (label, var) in enumerate({"Quantité": "entry_quantite", "Temps/pièce (min)": "entry_temps", "Livraison (YYYY-MM-DD)": "entry_livraison", "Priorité (1=urgent)": "entry_priorite"}.items()):
            ttk.Label(fenetre, text=label).grid(row=i, column=0, padx=5, pady=5)
            entry = ttk.Entry(fenetre)
            entry.grid(row=i, column=1, padx=5, pady=5)
            locals()[var] = entry

        ttk.Button(fenetre, text="Valider", command=valider).grid(row=4, column=0, columnspan=2, pady=10)

    def generer_planning(self):
        if not self.dossiers:
            messagebox.showwarning("Attention", "Aucun dossier à planifier")
            return
        self.planning = generer_planning(self.dossiers, self.machines, self.equipes)
        self.actualiser_treeview_planning()

    def actualiser_treeview_planning(self):
        for item in self.tree_planning.get_children():
            self.tree_planning.delete(item)
        for i, op in enumerate(self.planning):
            self.tree_planning.insert("", "end", iid=i, values=tuple(op.values()))

    def exporter_json(self):
        exporter_json(self.dossiers, self.planning)


### core/dossiers.py
def charger_donnees_test():
    return [
        {"nom": "Dossier 1", "quantite": 15, "temps_unitaire": 20, "livraison": "2025-06-19", "priorite": 2},
        {"nom": "Dossier 2", "quantite": 108, "temps_unitaire": 7, "livraison": "2025-06-13", "priorite": 1},
        {"nom": "Dossier 3", "quantite": 32, "temps_unitaire": 25, "livraison": "2025-06-22", "priorite": 3},
        {"nom": "Dossier 4", "quantite": 72, "temps_unitaire": 30, "livraison": "2025-06-26", "priorite": 4}
    ]


### core/planning.py
from datetime import datetime, timedelta

def generer_planning(dossiers, machines, equipes):
    dossiers_tries = sorted(dossiers, key=lambda x: (x["priorite"], x["livraison"]))
    planning = []
    date_courante = datetime.now().date()

    capacite_matin = 8
    capacite_apres_midi = 16

    for dossier in dossiers_tries:
        quantite = dossier["quantite"]
        temps = dossier["temps_unitaire"]
        nom = dossier["nom"]

        while quantite > 0:
            max_m1 = int(capacite_matin * 60 / temps)
            max_m2 = int(capacite_matin * 60 / (temps * 1.15))
            max_pm = int(capacite_apres_midi * 60 / temps)

            if temps > 4 and quantite > max_m1:
                q1 = min(max_m1, quantite)
                q2 = min(max_m2, quantite - q1)

                if q1:
                    planning.append({"date": str(date_courante), "equipe": "Matin", "machine": "M1", "dossier": nom, "quantite": q1, "debut": "06:00", "fin": "", "mode": "Normal"})
                    quantite -= q1
                if q2:
                    planning.append({"date": str(date_courante), "equipe": "Matin", "machine": "M2", "dossier": nom, "quantite": q2, "debut": "06:00", "fin": "", "mode": "Dégradé -15%"})
                    quantite -= q2

            if quantite > 0:
                qpm = min(max_pm, quantite)
                planning.append({"date": str(date_courante), "equipe": "Apres-midi", "machine": "M1+M2", "dossier": nom, "quantite": qpm, "debut": "14:00", "fin": "", "mode": "Normal"})
                quantite -= qpm

            if quantite > 0:
                date_courante += timedelta(days=1)

    return planning


### utils/export.py
import json
from tkinter import messagebox
from datetime import datetime

def exporter_json(dossiers, planning):
    export_data = {
        "dossiers": dossiers,
        "planning": planning,
        "resume": {
            "nb_operations": len(planning),
            "jours_utilises": len(set(op["date"] for op in planning)),
            "export_date": datetime.now().isoformat()
        }
    }
    try:
        with open("planning_export.json", "w", encoding="utf-8") as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)
        messagebox.showinfo("Succès", "Planning exporté vers 'planning_export.json'")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'export: {str(e)}")
