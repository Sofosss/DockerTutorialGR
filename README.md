<h1 align="center">
<br>
<img src="./images_media/docker-logo-white.png" alt="logo" style="width:200px;margin-bottom:4vh">
<br>
<strong> A GR Docker Tutorial for Beginners </strong>
</h1>

<h3 align="center">
<i>This repository serves as a beginner's tutorial on Docker in Greek. It provides concise guidance on Docker fundamentals, including the creation of Dockerfiles, building images, running containers and sharing images.</i>
</h3>
<br>

[![License][license-badge]][license-link]

# 🚩 Table of Contents
* [Εισαγωγή στο Docker](#docker-introduction)
* [Εγκατάσταση του Docker](#docker-installation)
* [Βασικές εντολές Docker](#docker-commands)
* [Δημιουργία Dockerfile](#dockerfile-creation)
* [Κατασκευή Εικόνας Docker](#docker-image-creation)
* [Διαχείριση Docker Images](#docker-images)
* [Docker Compose](#docker-compose)
* [Κατασκευή Docker Volume](#docker-volume-creation)
* [Διαχείριση Volumes](#docker-volumes)
* [Προχωρημένες λειτουργίες Docker](#Advanced-docker-func)
* [Case Studies](#Case-Studies)


# Εισαγωγή στο Docker
##  Τι είναι Docker 
Το Docker αποτελεί μια πλατφόρμα ανοικτού κώδικα που παρέχει εργαλεία για τον αυτοματισμό της διαδικασίας εγκατάστασης, ρύθμισης και εκτέλεσης εφαρμογών μέσω της χρήσης ελαφρών, φορητών εικονικών μηχανών, γνωστών ως "**containers**".

## Βασικά στοιχεία
1. **Containers**:
* Είναι εκτελέσιμα περιβάλλοντα(runtime environments) που περιλαμβάνουν την εφαρμογή και όλες τις απαραίτητες εξαρτήσεις της.
* Προσφέρουν απομόνωση, εξασφαλίζοντας ότι η εφαρμογή εκτελείται με τον ίδιο τρόπο, ανεξάρτητα από το περιβάλλον εκτέλεσης.
2. **Images**
* Αποτελούν εκτελέσιμα πακέτα που περιέχουν την εφαρμογή, τις εξαρτήσεις και τις "οδηγίες" εκτέλεσης.
* Οι εικόνες είναι ανεξάρτητες και μπορούν να κοινοποιούνται και να επαναχρησιμοποιούνται.
3. **Dockerfile**
* Αρχείο κειμένου που περιγράφει τα βήματα για τη δημιουργία μιας εικόνας Docker.
* Περιέχει οδηγίες για την επιλογή της εικόνας βάσης, την εγκατάσταση εξαρτήσεων, τον καθορισμό του working directory και του σημείου εκκίνησης(entrypoint) κ.ά.
4. **Docker Compose**
* Επιτρέπει τον ορισμό και τη διαχείριση πολλαπλών containers ως μέρος μιας εφαρμογής.
* Καθορίζει τις ρυθμίσεις, τις εξαρτήσεις και τις υπηρεσίες ενός περιβάλλοντος εκτέλεσης μέσω ενός YAML αρχείου. 
5. **Volumes**
* Διατηρούν και διαχειρίζονται δεδομένα μεταξύ του host machine και των containers.
* Χρησιμοποιούνται για την αποφυγή απώλειας δεδομένων κατά την ανανέωση ή αντικατάσταση ενός container.
6. **Networks**
* Επιτρέπουν την επικοινωνία μεταξύ διαφορετικών containers.
* Ορίζουν περιβάλλοντα δικτύου για την ασφαλή επικοινωνία μεταξύ διαφορετικών εφαρμογών.
7. **Docker Hub**
* Διαδικτυακή υπηρεσία που παρέχει την δυνατότητα αποθήκευσης, διαμοιρασμού και αναζήτησης εικόνων Docker.


# Εγκατάσταση του Docker

Για την εγκατάσταση του Docker engine στο προσωπικό σας μηχάνημα, θα πρέπει να ακολουθήσετε συγκεκριμένα βήματα, κατάλληλα προσαρμοσμένα στο λειτουργικό σύστημα που χρησιμοποιείτε.

* Αναλυτικές οδηγίες εγκατάστασης για **Windows**: [Docker Desktop for Windows][windows-link]
* Αναλυτικές οδηγίες εγκατάστασης για **Linux**(Ubuntu distr.): [Docker Desktop for Linux][linux-link]
* Αναλυτικές οδηγίες εγκατάστασης για **macOS**: [Docker Desktop for macOS][macos-link] 

Μόλις ολοκληρώσετε την εγκατάσταση του Docker, ελέγξτε ότι η τελευταία έγινε επιτυχημένα εκτελώντας την εντολή:
```bash
$ docker run hello-world
```
Προκειμένου να ελέγξετε την έκδοση του Docker που έχετε πλέον στο μηχάνημά σας, μπορείτε να χρησιμοποιήσετε την εντολή:
```bash
$ docker version
```

# Βασικές Εντολές Docker
***docker pull [desired image]***: Kατεβάζει την επιθυμητή εικόνα από το αντίστοιχο Docker registry(Docker Hub) και την αποθηκεύει στο σύστημα του χρήστη. Για παράδειγμα, εκτελώντας την εντολή:
```bash 
$ docker pull nginx 
```
κατεβάζουμε και αποθηκεύουμε την εικόνα nginx στο μηχάνημά μας. 

***docker images***: Εμφανίζει πληροφορίες σχετικές με τις εικόνες Docker που έχει αποθηκεύσει ο χρήστης στο σύστημά του. Εάν, νωρίτερα εκτελέσατε την εντολή αποθήκευσης της εικόνας nginx, τότε εκτελώντας την εντολή:
```bash 
$ docker images
```
θα πρέπει να λάβετε ως αποτέλεσμα μία λίστα με μία ή περισσότερες εικόνες(εάν έχετε ήδη και άλλες εικόνες αποθηκευμένες στο μηχάνημά σας), μεταξύ των οποίων περιλαμβάνεται και αυτή του nginx. 

***docker run [OPTIONS] IMAGE[:TAG] [COMMAND] [ARG...]***: Χρησιμοποιείται για την δημιουργία ενός container βάσει μιας συγκεκριμένης εικόνας. Αν επιθυμείται ο καθορισμός επιπλέον επιλογών, όπως το αν το container θα εκτελεστεί σε background ή interactive κατάσταση ή ο ορισμός συγκεκριμένων θυρών, παρέχεται η δυντότητα προσθήκης των επιλογών αυτών μετά το όνομα της εικόνας. Για παράδειγμα, εκτελώντας την εντολή:
```bash 
$ docker run -d --name my_first_container -p 8080:80 nginx 
```
 δημιουργούμε ένα container που ονομάζεται ***my_first_container*** και χρησιμοποιούμε το flag **-d** προκειμένου το container να εκτελείται στο background και το flag **-p 8080:80** προκειμένου να συνδέσουμε τη θύρα 8080 του τοπικού συστήματός μας με τη θύρα 80 του container.



<!-- MARKDOWN LINKS & IMAGES -->
[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg
[license-link]: https://github.com/DmMeta/ChordSeek/blob/main/LICENSE
[windows-link]:https://docs.docker.com/desktop/install/windows-install/
[linux-link]: https://docs.docker.com/engine/install/ubuntu/
[macos-link]: https://docs.docker.com/desktop/install/mac-install/