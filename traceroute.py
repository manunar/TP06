import subprocess

import argparse



def run_traceroute(target, progressive, output_file):
    # Détecter le système d'exploitation pour choisir la commande correcte
    command = ['tracert', target]  # Utiliser 'tracert' sur Windows

    if progressive:
        # Utiliser subprocess.Popen pour afficher les résultats au fur et à mesure
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            print(line.strip())
    else:
        # Utiliser subprocess.run pour attendre la fin du traceroute et afficher tout à la fois
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout.strip()
        print(output)

        # Si un fichier de sortie est spécifié, enregistrer les résultats dans le fichier
        # Modification de l'encodage lors de l'ouverture du fichier pour éviter les problèmes d'affichage
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(output)


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
