import subprocess
import argparse

def run_traceroute(target, progressive, output_file):
    command = ['tracert', target]  # Utiliser 'tracert' sur Windows

    if progressive:
        # Utiliser subprocess.Popen pour afficher les résultats au fur et à mesure
        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        except FileNotFoundError:
            print("Erreur : La commande 'tracert' est introuvable. Assurez-vous qu'elle est installée et accessible dans le PATH.")
            return
        except Exception as e:
            print(f"Une erreur est survenue lors de l'exécution de 'tracert': {e}")
            return

        try:
            for line in process.stdout:
                print(line.strip())
        except Exception as e:
            print(f"Une erreur est survenue lors de la lecture de la sortie du traceroute : {e}")
    else:
        # Utiliser subprocess.run pour attendre la fin du traceroute et afficher tout à la fois
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        except FileNotFoundError:
            print("Erreur : La commande 'tracert' est introuvable. Assurez-vous qu'elle est installée et accessible dans le PATH.")
            return
        except Exception as e:
            print(f"Une erreur est survenue lors de l'exécution de 'tracert': {e}")
            return

        output = result.stdout.strip()
        print(output)

        # Si un fichier de sortie est spécifié, enregistrer les résultats dans le fichier
        if output_file:
            try:
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(output)
            except PermissionError:
                print(f"Erreur : Impossible d'écrire dans le fichier '{output_file}' (Permissions insuffisantes).")
            except FileNotFoundError:
                print(f"Erreur : Le chemin spécifié pour le fichier '{output_file}' est invalide.")
            except Exception as e:
                print(f"Une erreur est survenue lors de l'écriture du fichier '{output_file}': {e}")

def main():
    # Définir les options du script avec argparse
    parser = argparse.ArgumentParser(description="Exécuter un traceroute sur une URL ou une adresse IP.")

    parser.add_argument('target', help="URL ou adresse IP à tracer.")
    parser.add_argument('-p', '--progressive', action='store_true', help="Afficher les résultats au fur et à mesure.")
    parser.add_argument('-o', '--output-file', type=str, help="Enregistrer les résultats dans un fichier.")

    args = parser.parse_args()

    # Exécuter le traceroute avec les options spécifiées
    run_traceroute(args.target, args.progressive, args.output_file)

if __name__ == '__main__':
    main()
