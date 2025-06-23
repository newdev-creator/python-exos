import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import json

class PlanificateurProduction:
    def __init__(self, root):
        self.root = root
        self.root.title("Planificateur de Production")
        self.root.geometry("1200x800")
        
        # Données
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
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Section Dossiers
        ttk.Label(main_frame, text="Dossiers de Production", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=4, pady=10)
        
        # Treeview pour les dossiers
        self.tree_dossiers = ttk.Treeview(main_frame, columns=("quantite", "temps_unitaire", "temps_total", "livraison", "priorite"), show="headings", height=6)
        self.tree_dossiers.heading("quantite", text="Quantité")
        self.tree_dossiers.heading("temps_unitaire", text="Temps/pièce (min)")
        self.tree_dossiers.heading("temps_total", text="Temps total (h)")
        self.tree_dossiers.heading("livraison", text="Livraison")
        self.tree_dossiers.heading("priorite", text="Priorité")
        
        for col in self.tree_dossiers["columns"]:
            self.tree_dossiers.column(col, width=100)
            
        self.tree_dossiers.grid(row=1, column=0, columnspan=4, pady=10, sticky=(tk.W, tk.E))
        
        # Boutons
        ttk.Button(main_frame, text="Ajouter Dossier", command=self.ajouter_dossier).grid(row=2, column=0, padx=5)
        ttk.Button(main_frame, text="Générer Planning", command=self.generer_planning).grid(row=2, column=1, padx=5)
        ttk.Button(main_frame, text="Exporter JSON", command=self.exporter_json).grid(row=2, column=2, padx=5)
        
        # Séparateur
        ttk.Separator(main_frame, orient="horizontal").grid(row=3, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=20)
        
        # Section Planning
        ttk.Label(main_frame, text="Planning Généré", font=("Arial", 12, "bold")).grid(row=4, column=0, columnspan=4, pady=10)
        
        # Treeview pour le planning
        self.tree_planning = ttk.Treeview(main_frame, columns=("date", "equipe", "machine", "dossier", "quantite", "debut", "fin", "mode"), show="headings", height=10)
        
        headings = {
            "date": "Date",
            "equipe": "Équipe", 
            "machine": "Machine",
            "dossier": "Dossier",
            "quantite": "Quantité",
            "debut": "Début",
            "fin": "Fin",
            "mode": "Mode"
        }
        
        for col, text in headings.items():
            self.tree_planning.heading(col, text=text)
            self.tree_planning.column(col, width=80)
            
        self.tree_planning.grid(row=5, column=0, columnspan=4, pady=10, sticky=(tk.W, tk.E))
        
        # Zone de résumé
        self.text_resume = tk.Text(main_frame, height=8, width=80)
        self.text_resume.grid(row=6, column=0, columnspan=4, pady=10, sticky=(tk.W, tk.E))
        
    def charger_donnees_test(self):
        """Charge les données de test"""
        dossiers_test = [
            {"nom": "Dossier 1", "quantite": 15, "temps_unitaire": 20, "livraison": "2025-06-19", "priorite": 2},
            {"nom": "Dossier 2", "quantite": 108, "temps_unitaire": 7, "livraison": "2025-06-13", "priorite": 1},
            {"nom": "Dossier 3", "quantite": 32, "temps_unitaire": 25, "livraison": "2025-06-22", "priorite": 3},
            {"nom": "Dossier 4", "quantite": 72, "temps_unitaire": 30, "livraison": "2025-06-26", "priorite": 4}
        ]
        
        for dossier in dossiers_test:
            self.dossiers.append(dossier)
            
        self.actualiser_treeview_dossiers()
        
    def actualiser_treeview_dossiers(self):
        """Met à jour l'affichage des dossiers"""
        for item in self.tree_dossiers.get_children():
            self.tree_dossiers.delete(item)
            
        for i, dossier in enumerate(self.dossiers):
            temps_total = round(dossier["quantite"] * dossier["temps_unitaire"] / 60, 2)
            self.tree_dossiers.insert("", "end", iid=i, values=(
                dossier["quantite"],
                dossier["temps_unitaire"], 
                temps_total,
                dossier["livraison"],
                dossier["priorite"]
            ))
            
    def ajouter_dossier(self):
        """Interface pour ajouter un dossier"""
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
                messagebox.showerror("Erreur", "Veuillez saisir des valeurs numériques valides")
        
        fenetre = tk.Toplevel(self.root)
        fenetre.title("Ajouter un Dossier")
        fenetre.geometry("300x200")
        
        ttk.Label(fenetre, text="Quantité:").grid(row=0, column=0, padx=5, pady=5)
        entry_quantite = ttk.Entry(fenetre)
        entry_quantite.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(fenetre, text="Temps/pièce (min):").grid(row=1, column=0, padx=5, pady=5)
        entry_temps = ttk.Entry(fenetre)
        entry_temps.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(fenetre, text="Livraison (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
        entry_livraison = ttk.Entry(fenetre)
        entry_livraison.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(fenetre, text="Priorité (1=urgent):").grid(row=3, column=0, padx=5, pady=5)
        entry_priorite = ttk.Entry(fenetre)
        entry_priorite.grid(row=3, column=1, padx=5, pady=5)
        
        ttk.Button(fenetre, text="Valider", command=valider).grid(row=4, column=0, columnspan=2, pady=10)
        
    def generer_planning(self):
        """Algorithme principal de planification"""
        if not self.dossiers:
            messagebox.showwarning("Attention", "Aucun dossier à planifier")
            return
            
        # Trier par priorité puis par date de livraison
        dossiers_tries = sorted(self.dossiers, key=lambda x: (x["priorite"], x["livraison"]))
        
        # Initialiser le planning
        self.planning = []
        date_courante = datetime.now().date()
        
        # Capacités par équipe/jour
        capacite_matin = 8  # 1 opérateur, 8h
        capacite_apres_midi = 16  # 2 opérateurs, 8h chacun
        
        for dossier in dossiers_tries:
            quantite_restante = dossier["quantite"]
            temps_unitaire = dossier["temps_unitaire"]
            
            while quantite_restante > 0:
                # Calculer les quantités possibles par créneaux
                pieces_possible_matin_1_machine = int(capacite_matin * 60 / temps_unitaire)
                pieces_possible_matin_2_machines = int(capacite_matin * 60 / (temps_unitaire * 1.15))  # Mode dégradé
                pieces_possible_apres_midi = int(capacite_apres_midi * 60 / temps_unitaire)
                
                # Stratégie: utiliser le matin avec 2 machines si temps_unitaire > 4min
                if temps_unitaire > 4 and quantite_restante > pieces_possible_matin_1_machine:
                    # Matin avec 2 machines
                    qty_m1 = min(pieces_possible_matin_1_machine, quantite_restante)
                    qty_m2 = min(pieces_possible_matin_2_machines, quantite_restante - qty_m1)
                    
                    if qty_m1 > 0:
                        self.planning.append({
                            "date": date_courante.strftime("%Y-%m-%d"),
                            "equipe": "Matin",
                            "machine": "M1", 
                            "dossier": dossier["nom"],
                            "quantite": qty_m1,
                            "debut": "06:00",
                            "fin": f"{6 + qty_m1 * temps_unitaire // 60:02d}:{(qty_m1 * temps_unitaire) % 60:02d}",
                            "mode": "Normal"
                        })
                        quantite_restante -= qty_m1
                        
                    if qty_m2 > 0 and quantite_restante > 0:
                        self.planning.append({
                            "date": date_courante.strftime("%Y-%m-%d"),
                            "equipe": "Matin", 
                            "machine": "M2",
                            "dossier": dossier["nom"],
                            "quantite": qty_m2,
                            "debut": "06:00",
                            "fin": f"{6 + int(qty_m2 * temps_unitaire * 1.15) // 60:02d}:{int(qty_m2 * temps_unitaire * 1.15) % 60:02d}",
                            "mode": "Dégradé -15%"
                        })
                        quantite_restante -= qty_m2
                        
                # Après-midi
                if quantite_restante > 0:
                    qty_apres_midi = min(pieces_possible_apres_midi, quantite_restante)
                    self.planning.append({
                        "date": date_courante.strftime("%Y-%m-%d"),
                        "equipe": "Apres-midi",
                        "machine": "M1+M2",
                        "dossier": dossier["nom"], 
                        "quantite": qty_apres_midi,
                        "debut": "14:00",
                        "fin": f"{14 + qty_apres_midi * temps_unitaire // 60:02d}:{(qty_apres_midi * temps_unitaire) % 60:02d}",
                        "mode": "Normal"
                    })
                    quantite_restante -= qty_apres_midi
                    
                # Passer au jour suivant
                if quantite_restante > 0:
                    date_courante += timedelta(days=1)
        
        self.actualiser_treeview_planning()
        self.generer_resume()
        
    def actualiser_treeview_planning(self):
        """Met à jour l'affichage du planning"""
        for item in self.tree_planning.get_children():
            self.tree_planning.delete(item)
            
        for i, operation in enumerate(self.planning):
            self.tree_planning.insert("", "end", iid=i, values=(
                operation["date"],
                operation["equipe"],
                operation["machine"],
                operation["dossier"],
                operation["quantite"],
                operation["debut"],
                operation["fin"],
                operation["mode"]
            ))
            
    def generer_resume(self):
        """Génère un résumé du planning"""
        self.text_resume.delete(1.0, tk.END)
        
        resume = "=== RÉSUMÉ DU PLANNING ===\n\n"
        
        # Analyse par dossier
        dossiers_stats = {}
        for operation in self.planning:
            dossier = operation["dossier"]
            if dossier not in dossiers_stats:
                dossiers_stats[dossier] = {"quantite": 0, "dernier_jour": operation["date"]}
            dossiers_stats[dossier]["quantite"] += operation["quantite"]
            dossiers_stats[dossier]["dernier_jour"] = max(dossiers_stats[dossier]["dernier_jour"], operation["date"])
            
        for dossier_original in self.dossiers:
            nom = dossier_original["nom"]
            if nom in dossiers_stats:
                stats = dossiers_stats[nom]
                livraison = datetime.strptime(dossier_original["livraison"], "%Y-%m-%d").date()
                fin_prod = datetime.strptime(stats["dernier_jour"], "%Y-%m-%d").date()
                
                statut = "✓ À TEMPS" if fin_prod <= livraison else "⚠ RETARD"
                ecart = (fin_prod - livraison).days
                
                resume += f"{nom}: {stats['quantite']}/{dossier_original['quantite']} pièces - Fin: {stats['dernier_jour']} - {statut}"
                if ecart != 0:
                    resume += f" ({ecart:+d} jours)"
                resume += "\n"
                
        # Utilisation machines
        jours_utilises = len(set(op["date"] for op in self.planning))
        resume += f"\nUtilisation: {jours_utilises} jour(s) de production\n"
        resume += f"Nombre d'opérations: {len(self.planning)}\n"
        
        # Mode dégradé
        operations_degradees = sum(1 for op in self.planning if "Dégradé" in op["mode"])
        if operations_degradees > 0:
            resume += f"Opérations en mode dégradé: {operations_degradees}\n"
            
        self.text_resume.insert(1.0, resume)
        
    def exporter_json(self):
        """Exporte le planning au format JSON"""
        if not self.planning:
            messagebox.showwarning("Attention", "Aucun planning à exporter")
            return
            
        export_data = {
            "dossiers": self.dossiers,
            "planning": self.planning,
            "resume": {
                "nb_operations": len(self.planning),
                "jours_utilises": len(set(op["date"] for op in self.planning)),
                "export_date": datetime.now().isoformat()
            }
        }
        
        try:
            with open("planning_export.json", "w", encoding="utf-8") as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("Succès", "Planning exporté vers 'planning_export.json'")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'export: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlanificateurProduction(root)
    root.mainloop()