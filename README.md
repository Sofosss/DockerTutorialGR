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
* [Εισαγωγή στο Docker](#εισαγωγή-στο-docker)
* [Εγκατάσταση του Docker](#εγκατάσταση-του-docker)
* [Βασικές εντολές Docker](#βασικές-εντολές-docker)
* [Κατασκευή εικόνας Docker μέσω Dockerfile](#κατασκευή-εικόνας-docker-μέσω-dockerfile)
* [Docker Volumes](#docker-volume)
* [Docker Networking](#docker-networking)
* [Case Study](#case-study)
* [Contact](#Contact)
* [License](#License)

# Εισαγωγή στο Docker
##  Τι είναι το Docker 
Το Docker αποτελεί μια πλατφόρμα ανοικτού κώδικα που παρέχει ένα σύνολο εργαλείων για τον αυτοματισμό της διαδικασίας ανάπτυξης, δοκιμής, εγκατάστασης, ρύθμισης και εκτέλεσης εφαρμογών μέσω της χρήσης ελαφρών(lightweight), φορητών εικονικών μηχανών, γνωστών ως "**containers**".


## Βασικά στοιχεία
1. **Docker Engine(Docker Client & Server)**
* Η αρχιτεκτονική του Docker, όπως αποτυπώνεται παρακάτω στην εικόνα που ακολουθεί, έχει client-server δομή.
* Το/Τα Docker client(s) επικοινωνεί/ούν με τον Docker server(daemon), ο οποίος είναι υπέυθυνος για όλες
τις επιμέρους λειτουργίες του Docker.
* Το Docker περιέχει ένα CLI(command line) εργαλείο, καθώς και ένα πλήρες RestFul API για την επικοινωνία με τον Docker daemon.

2. **Docker Images**
* Αποτελούν εκτελέσιμα πακέτα που περιέχουν την εφαρμογή, τις εξαρτήσεις και τις "οδηγίες" εκτέλεσης. Πρόκειται, ουσιαστικά για τον πυρήνα - blueprint των docker containers.
* Οι εικόνες είναι αυτόνομες και μπορούν να κοινοποιούνται και να επαναχρησιμοποιούνται.
* Συνήθως οι εικόνες δημιουργούνται μέσω **Dockerfile** αρχείων. Πρόκειται για ένα είδος YAML αρχείου που περιγράφει τα βήματα για τη δημιουργία μιας εικόνας Docker. Περιέχει οδηγίες για την επιλογή της εικόνας βάσης, την εγκατάσταση εξαρτήσεων, τον καθορισμό του working directory και του σημείου εκκίνησης(entrypoint) κ.ά.

3. **Docker containers**
* Πρόκειται για πλήρως αυτόνομα περιβάλλοντα εκτέλεσης(runtime environments) που ενθυλακώνουν την εφαρμογή-υπηρεσία και όλες τις απαραίτητες εξαρτήσεις της. 
* Παρέχουν απομόνωση, εξασφαλίζοντας ότι η εφαρμογή εκτελείται σε ένα φορητό και ανεξάρτητο 
περιβάλλον, εξαλείφοντας με αυτόν τον τρόπο πιθανά προβλήματα ασυμβατότητας συστημάτων. Δηλαδή, είναι 
σχεδιασμένα έτσι ώστε να μπορούν να αναπτυχθούν ή να εκτελεστούν σε έναν προσωπικό υπολογιστή, σε έναν cluster στο Cloud, σε έναν virtual server ή γενικότερα σε οποιοδήποτε άλλο υπολογιστικό σύστημα.

4. **Docker Registry**
* Το Docker αποθηκεύει και κατανέμει τα διάφορα Docker images σε αποθετήρια, τόσο δημόσια όσο και ιδιωτικά. 
* Η εταιρία Docker, Inc. υποστηρίζει την κοινότητα διατηρώντας το DockerHub, το μεγαλύτερο αποθετήριο για Docker images. Πρόκειται, για μία διαδικτυακή υπηρεσία που παρέχει την δυνατότητα αποθήκευσης, διαμοιρασμού και αναζήτησης εικόνων Docker, τόσο δημοσίων όσο και ιδιωτικών.
* Ωστόσο, υπάρχει κι η δυνατότητα για κάποιον οργανισμό να υποστηρίξει ανεξάρτητο, ιδιωτικό Registry πίσω από το firewall του.

</br>
</br>


<p align="center">
 <img src="./images_media/docker_architecture.gif"  alt="docker_architecture" width = 80%>
    <br>
    <em><i>Gif source: </i><a href="https://vikasrajput.hashnode.dev/" alt = "Vikas Rajputin site">Vikas Rajputin</a></em>
</p>
</br>

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
> [!WARNING]
> Επειδή το Docker χρησιμοποιεί ***Unix socket*** το οποίο ανήκει στον root χρήστη του μηχανήματος, η χρήση του Docker CLI(Command Line) απαιτεί την
χρήση του προσδιορισμού ***sudo***. Σε περίπτωση που κάτι τέτοιο δεν είναι επιθυμητό, χρειάζεται να προσθέσετε τον αντίστοιχο
χρήστη σε ένα ***Unix group*** με την ονομασία **docker**. Η παραπάνω διαδικασία μπορεί να διεκπεραιωθεί μέσω της εκτέλεσης των παρακάτω εντολών:

```bash
# Δημιουργία του group docker(αν δεν υπάρχει ήδη)
$ sudo groupadd docker

# Προσθήκη του χρήστη στο group docker
$ sudo usermod -aG docker $USER

# Ενεργοποίηση αλλαγών για τα groups κάνοντας relogin και ελέγχος χρήσης docker χωρίς sudo
$ docker run hello-world
``` 
> [!CAUTION]
> Η εισαγωγή ενός χρήστη στο group Docker, του αναθέτει αυτόματα δικαιώματα επιπέδου διαχειριστή(root privileges). Επομένως, απαιτείται ιδιαίτερη προσοχή στους χρήστες που εισέρχονται στο συγκεκριμένο group.

> [!NOTE]
> Παρέχεται και η δυνατότητα χρήσης του Docker σε rootless mode. 
Περισσότερες πληροφορίες μπορούν να αντληθούν από το επίσημο documentation του [Docker][Docker-rootless].


# Βασικές Εντολές Docker
✨***docker pull [desired image]***: Kατεβάζει την επιθυμητή εικόνα από το προεπιλεγμένο Docker registry(από το Docker Hub στην default περίπτωση) και την αποθηκεύει στο σύστημα του χρήστη. Για παράδειγμα, εκτελώντας την εντολή:
```bash 
$ docker pull nginx 
```
κατεβάζουμε και αποθηκεύουμε την εικόνα nginx στο μηχάνημά μας. 

✨***docker images***: Εμφανίζει πληροφορίες σχετικές με τις εικόνες Docker που έχει ο χρήστης στο σύστημά του. Εάν, νωρίτερα εκτελέσατε την εντολή αποθήκευσης της εικόνας nginx, τότε εκτελώντας την εντολή:
```bash 
$ docker images
```
θα πρέπει να λάβετε ως αποτέλεσμα μία λίστα με μία ή περισσότερες εικόνες(εάν έχετε ήδη και άλλες εικόνες στο μηχάνημά σας), μεταξύ των οποίων περιλαμβάνεται και αυτή του Nginx. 

✨***docker run [OPTIONS] IMAGE[:TAG] [COMMAND] [ARG...]***: Χρησιμοποιείται για την δημιουργία ενός container βάσει μιας συγκεκριμένης εικόνας. Αν είναι επιθυμητός ο καθορισμός επιπλέον επιλογών, παρέχεται η δυνατότητα χρήσης επιπλέον ορισμάτων. Αυτά καθορίζουν λειτουργίες όπως το αν το container θα εκτελεστεί σε background ή interactive κατάσταση, το port-forwading συγκεκριμένων θυρών, ο μηχανισμός των logs(logging driver), κ.ά. Για παράδειγμα, εκτελώντας την εντολή:
```bash 
$ docker run -d --name my_first_container -p 8080:80 nginx 
```
 δημιουργούμε ένα container που ονομάζεται ***my_first_container*** και χρησιμοποιούμε το flag **-d** προκειμένου το container να εκτελείται στο background, χωρίς να βλέπουμε το αποτέλεσμα πιθανής εξόδου στην οθόνη και το flag **-p 8080:80** προκειμένου να συνδέσουμε τη θύρα 8080 του host συστήματος με τη θύρα 80 του container.

✨***docker ps***: Εμφανίζει μία λίστα με τα ενεργά containers μαζί με πληροφορίες για αυτά, όπως το container ID, το όνομα, την κατάσταση του container, τις πόρτες που χρησιμοποιεί κ.ά.
Για παράδειγμα, εκτελώντας, στο προσωπικό μας μηχάνημα την εντολή:
```bash 
$ docker ps 
```
θα λάβουμε ως επιστροφή μία λίστα όπως η παρακάτω:
<figure markdown="1" style="display:flex;align-items:center;flex-direction:column;padding:2vh;">
<img src="./images_media/docker_ps.png"  alt="docker_ps result img" >
</figure>

Παρατηρούμε πως έχουμε ένα ενεργό container(πρόκειται για εκείνο που δημιουργήσαμε νωρίτερα), το οποίο στηρίζεται στην εικόνα του **Nginx** και "ακούει" στην θύρα 80.

✨***docker ps -a***: Εμφανίζει μία λίστα με όλα τα containers του συστήματος του χρήστη μαζί με τις αντίστοιχες πληροφορίες τους.

✨***docker stop [OPTIONS] CONTAINER [CONTAINER...]***: Χρησιμοποιείται για να σταματήσει ένα ενεργό container. Όταν εκτελεστεί αυτή η εντολή, το Docker στέλνει ένα σήμα(SIGTERM) στις διεργασίες που τρέχουν εντός του container, προκειμένου να προετοιμαστούν για τον τερματισμό τους. Αν η μία από τις διαδικασίες αυτές δεν τερματίσει εθελοντικά, τότε έπειτα από ένα χρονικό όριο, το Docker στέλνει ένα SIGKILL για να την εξαναγκάσει να τερματίσει. Με άλλα λόγια, η εντολή docker stop σταματά ενα container, επιτρέποντάς του να ολοκληρώσει τις εκκρεμότητές του πριν τεθεί σε ανενεργή κατάσταση. Για παράδειγμα, εκτελώντας την εντολή:
```bash 
$ docker stop my_first_container 
```
  σταματά το container ***"my_first_container"*** και τίθεται σε ανενεργή κατάσταση. Η ανενεργή κατάσταση του container μπορεί να επιβεβαιωθεί μέσω της εκτέλεσης της εντολής **docker ps -a**.


✨***docker start [OPTIONS] CONTAINER [CONTAINER...]***: Χρησιμοποιείται για την εκκίνηση ενός προηγουμένως δημιουργημένου, αλλά σταματημένου container. Όταν ένα container τερματίζεται(σταματημένο), τότε σταματά να εκτελείται και έτσι δεν καταναλώνει πόρους του συστήματος. Η εντολή docker start επανεκκινεί το container, επιτρέποντάς του να να εκκινήσει ξανά την εκτέλεσή του. Για παράδειγμα, εκτελώντας την εντολή:
```bash 
$ docker start my_first_container 
```
εκκινείται το container ***"my_first_container"*** και τίθεται σε ενεργή κατάσταση. Η ενεργή κατάσταση του container μπορεί να επιβεβαιωθεί μέσω της εκτέλεσης της εντολής **docker ps**.

✨***docker exec [OPTIONS] CONTAINER COMMAND [ARG...]***: Χρησιμοποιείται για την εκτέλεση εντολών εντός ενός ενεργού container. Επιτρέπει έτσι στους χρήστες να εκτελούν εντολές ή να αλληλεπιδρούν με το εσωτερικό περιβάλλον ενός container. Για παράδειγμα, εκτελώντας την εντολή:
```bash 
$ docker exec my_first_container nginx -v
```
λαμβάνουμε την έκδοση του Nginx server που εκτελείται μέσα στο container ***"my_first_container"***. 

✨***docker attach [OPTIONS] CONTAINER***: Χρησιμοποιείται για την σύνδεση του χρήστη με τα I/O streams του τερματικού ενός ενεργού container, επιτρέποντάς την απευθείας επικοινωνία του με το περιβάλλον εκτέλεσης του container. Για παράδειγμα, εκτελώντας τις εντολές:
```bash 
$ docker attach my_first_container 
$ curl -sSL http://127.0.0.1:8080
```
συνδεόμαστε στο stdout της διεργασίας nginx του container ***"my_first_container"*** και παρατηρούμε το αίτημα που έλαβε ο nginx server 
του container από την εκτέλεση της δεύτερης εντολής.

> [!NOTE]
> Η εκτέλεση της εντολής docker attach μπορεί να μοιάζει κάποιες φορές ως μη απόκριση του συστήματος, αλλά αυτό μπορεί να οφείλεται
στην έλλειψη δεδομένων στο Ι/Ο stream του τερματικού στο οποίο συνδέθηκε.

> [!IMPORTANT]
> Επειδή με την εντολή **docker attach** γίνεται σύνδεση πχ στο stdout της διεργασίας του container, ο τερματισμός της τρέχουσας διεργασίας(με τη χρήση CTRL + C - σήμα SIGINT) ισοδυναμεί επίσης και με τον τερματισμό του container. 

✨***docker inspect [OPTIONS] NAME|ID [NAME|ID...]***: Επιστρέφει ένα JSON αντικείμενο που περιέχει λεπτομερείς πληροφορίες για ένα ή περισσότερα αντικείμενα Docker, όπως είναι containers, images, networks και volumes. 

✨***docker logs [OPTIONS] CONTAINER***: Χρησιμοποιείται για την εμφάνιση των δεδομένων κάποιου I/O stream της διεργασίας ενός ενεργού ή πρόσφατα τερματισμένου container, σύμφωνα με τον logging driver που έχει οριστεί για αυτό. Αν δεν επιλεχθεί κάποια πιο σύνθετη ρύθμιση,
η εντολή δείχνει την έξοδο στο stdout της διεργασίας του container αυτού.

✨***docker rm [OPTIONS] CONTAINER [CONTAINER...]***: Χρησιμοποιείται για την διαγραφή ενός ή περισσότερων containers που έχουν τερματιστεί από το σύστημα. Χρησιμοποιείται, επομένως, για την αφαίρεση των container instances που δεν χρειάζεται ο χρήστης πλέον. Για παράδειγμα, εκτελώντας την εντολή:
```bash 
$ docker rm my_first_container 
```
θα διαγράψουμε το container με το όνομα **"my_first_container"**. Εάν θέλουμε να διαγράψουμε περισσότερα από ένα container, τοποθετούμε τα ονόματά τους ως επιπλέον ορίσματα. Η διαγραφή του container μπορεί να επιβεβαιωθεί μέσω της εκτέλεσης της εντολής **docker ps**.

> [!TIP]
> Χρησιμοποιώντας το flag -f στην εντολή **docker rm -f my_first_container** το container ***"my_first_container"*** θα διαγραφεί ακόμη και αν είναι ενεργό, αλλά αυτό ενδεχομένως να οδηγήσει σε απώλεια δεδομένων ή προβλήματα, αν δεν έχει εκτελεστεί προηγουμένως κατάλληλος έλεγχος.

# Κατασκευή εικόνας Docker μέσω Dockerfile

Όπως αναφέρθηκε νωρίτερα, ένα Dockerfile είναι ένα αρχείο τύπου YAML με ένα σύνολο από βήματα(instructions) μιας γλώσσας ειδικού πεδίου(Domain Specific language) που κατευθύνουν τη δημιουργία μιας εικόνας Docker. 

Για να γίνει κατανοητός ο τρόπος με τον οποίο δομείται ένα τέτοιο αρχείο, θα δημιουργηθεί ένα [Dockerfile][dockerfile-cstd1] για την κατασκευή εικόνας η οποία θα περιγράφει το container μίας απλής [Web εφαρμογής][node-app]. Πιο συγκεκριμένα, θα γίνει deploy ένα container τοπικά, στο οποίο θα εκτελείται μία εφαρμογή γραμμένη με Express-Node.js, σκοπός της οποίας είναι η εξυπηρέτηση ενός endpoint. Σ'αυτό, η εφαρμογή θα δέχεται HTTP POST αιτήσεις με δεδομένα σε μορφή JSON, τα οποία ακολούθως θα αποθηκεύει στον server. 

Το αρχείο Dockerfile δομείται ως εξής:

```bash
# Χρησιμοποιούμε μια επίσημη εικόνα του Node.js ως βάση. Το tag latest προσδιορίζει ότι "κατεβάζουμε" την πιο πρόσφατα διαθέσιμη επίσημη εικόνα Node.js
FROM node:latest

# Metadata στην εικόνα
LABEL maintainer="Argiris Sofotasios & Dimitris Metaxakis"
LABEL description="A simple Web app."

# Ορισμός environment variable για χρήση της από την εφαρμογή
ENV NODE_PORT=8891

# Δηλώνουμε τον φάκελο εργασίας στο περιβάλλον του container
WORKDIR /app

# Αντιγράφουμε τα αρχεία της εφαρμογής στον container
COPY . /app

# Εγκατάσταση των απαραίτητων βιβλιοθηκών
RUN npm install express body-parser

# Καθορισμός της θύρας που θα ακούει το container
EXPOSE 8891

# Κατά την εκκίνηση του container τρέχει ο server καλώντας το binary executable του nodejs
ENTRYPOINT ["node", "server.js"]
```

Δημιουργία της εικόνας **nodejs_server**:
```bash
cd ./casestudies/CaseStudy1/src
docker build -t nodejs_server:v0.1 .
```
> [!NOTE]
> Ο προσδιορισμός . ενημερώνει τον docker deamon για το build context της εικόνας, δηλαδή το σύνολο των αρχείων και φακέλων που εντοπίζονται σε αυτό. Την πληροφορία αυτή την χρησιμοποιεί ο deamon μεταξύ άλλων για την πρόσβαση σε αρχεία που μπορεί να χρησιμοποιούνται από εντολές στο Dockerfile καθώς και για την αποδοτική δημιουργία νέων εικονών με την χρήση έξυπνων caching μηχανισμών. 

Δημιουργία και εκτέλεση του container **express_server**:
```bash
docker run -d --name express_server -p 8080:8891 nodejs_server:v0.1 
```

# Docker Volumes

Στον κορμό του, ένα Docker container χρησιμοποιεί ένα πολυεπίπεδο ιεαραρχικό σύστημα αρχείων(layered file system). Κάθε επίπεδο-στρώμα αντιπροσωπεύει ένα σύνολο από αλλαγές στα αρχεία. Τα επίπεδα αυτά στοιβάζονται το ένα πάνω στο άλλο με σκοπό την δημιουργία του τελικού συστήματος αρχείων του container.
Μολονότι αυτή η προσέγγιση έχει ένα πλήθος πλεονεκτημάτων, μια βασική της αδυναμία είναι η διαγραφή των επιπέδων αυτών και των αντίστοιχων αρχείων κατά την διαγραφή ενός container.

<br>
<p align="center">
 <img src="./images_media/layer_fs_2.png"  alt="docker_architecture" width = 80%>
    <br>
    <em><i>Layered FS visualization</i></em>
</p>
</br>

Τα docker volumes είναι ένας μηχανισμός που εισάγεται για την διαχείριση του ζητήματος αυτού, καθώς αυτά παρακάμπτουν το ιεραρχικό σύστημα αρχείων. Πρόκειται για ειδικά ορισμένους καταλόγους που έχουν σκοπό τον διαμοιρασμό και την διατήρηση δεδομένων μεταξύ των διαφόρων containers, ανεξάρτητα από τον κύκλο ζωής τους. 

Στην δική μας εφαρμογή, o server αποθηκεύει τα δεδομένα των εισερχόμενων HTTP αιτήσεων σε ένα JSON αρχείο. Επειδή το αρχείο αυτό είναι αποθηκευμένο σε ένα στρώμα(layer) στο περιβάλλον του container, όταν το container διαγραφτεί, θα διαγραφτεί κι αυτό μαζί του. Συνεπώς, θα χάσουμε τα δεδομένα του server. Για να αποφευχθεί η ανεπιθύμητη αυτή κατάσταση, δημιουργούμε έναν καινούριο κατάλογο ***data_per***, δημιουργούμε ένα volume, έτσι ώστε να κάνουμε mount(συνδέσουμε) τον τοπικό κατάλογό μας ***CaseStudy1/data_per*** στον κατάλογο ***opt/data_per*** του container, εκτελώντας την παρακάτω εντολή κατά τη δημιουργία του container:

```bash
cd ./case_studies/CaseStudy1/
mkdir data_per
docker run -d --name express_server -p 8080:8891 --mount type=bind,source="$(pwd)"/data_per,target=/opt/data_per nodejs_server:v0.1    
```
Ισοδύναμα η τρίτη εντολή μπορεί να γραφτεί και ως εξής:

```bash
docker run -d --name express_server -p 8080:8891 -v "$(pwd)"/data_per:/opt/data_per nodejs_server:v0.1   
```

Με τον τρόπο αυτό δημιουργούμε ένα **bind mount**. Πρόκειται για μια γρήγορη τεχνική που χρησιμοποιείται συχνά από τους developers, ωστόσο η λειτουργία της στηρίζεται σε μεγάλο βαθμό στη δομή του συστήματος αρχείων(FS) του host με αποτέλεσμα να προκαλεί σημαντικά προβλήματα απόδοσης. 

Εκτός από τα bind mounts που καθορίζονται συναρτήσει της ύπαρξης ενός container, υπάρχει και η δυνατότητα δημιουργίας volumes ανεξάρτητα από τα διάφορα containers. 

Τέτοιου είδους volumes μπορούν να δημιουργηθούν με την εκτέλεση της εντολής:

```bash
docker volume create [volume name]
```
Όλα τα volumes που διαθέτει ο χρήστης στο σύστημά του μπορούν να εμφανιστούν με την εκτέλεση της εντολής:

```bash
docker volume ls
```
ενώ η επισκόπηση των πληροφοριών ενός συγκεκριμένου volume είναι εφικτή μέσω της εκτέλεσης της εντολής:

```bash
docker volume inspect [volume name]
```
Τέλος η διαγραφή ενός volume, εφόσον δεν υπάρχει ενεργό container που να το χρησιμοποιεί, πραγματοποιείται με την εκτέλεση της εντολής:

```bash
docker volume rm [volume name]
```


# Docker Networking

Το Docker Networking εισήχθει στην έκδοση 1.9 επιτρέποντας την εκτενή εξατομίκευση της δικτύωσης μεταξύ των containers.
Το Docker πλέον παρέχει την δυνατότητα ορισμού προσαρμοσμένων δικτύων από το χρήστη, καθιστώντας έτσι δυνατή την σύνδεση πολλαπλών containers στο ίδιο δίκτυο. Κάθε container έχει τη δική του διεύθυνση IP και το δικό του namespace εντός του δικτύου στο οποίο ανήκει. Αφού συνδεθούν στο user-defined δίκτυο, τα containers μπορούν να επικοινωνούν μεταξύ τους χρησιμοποιώντας τις IP διευθύνσεις τους ή τα ονόματά τους, τα οποία διαχειρίζονται πλήρως από ένα σύστημα ονοματοδοσίας(DNS) του Docker. 

Το Docker Networking είναι pluggable, παρέχοντας ένα σύνολο από Drivers, κάθε ένας εκ των οποίων προσφέρει εξειδικευμένη λειτουργικότητα. Οι πιο δημοφιλείς από αυτούς είναι:

* Bridge: Πρόκειται για τον προκαθορισμένο(default) network driver. Συνήθως χρησιμοποιείται σε περιπτώσεις που υπάρχει ανάγκη επικοινωνίας μεταξύ διαφορετικών containers του ίδιου host. Είναι μία συσκευή επιπέδου ζεύξης που προωθεί την κίνηση μεταξύ τμημάτων δικτύου. Ο Docker bridge driver εγκαθιστά αυτόματα κανόνες στο σύστημα του host, ούτως ώστε τα containers που ανήκουν σε διαφορετικά bridged networks να μην μπορούν να επικοινωνήσουν άμεσα μεταξύ τους. Κατά την εκκίνηση του Docker, δημιουργείται ένα προεπιλεγμένο bridged δίκτυο στο οποίο συνδέονται όλα τα containers. Κάτι τέτοιο παύει να ισχύει, εάν ο χρήστης καθορίσει το δίκτυο που θα συνδεθεί το αντίστοιχο container.

* Host: Άρει την συνθήκη απομόνωσης της στοίβας δικτύου του αντίστοιχου container, το οποίο πλέον δεν έχει δική του IP διεύθυνση αλλά μοιράζεται το ίδιο namespace δικτύου με τον host, χωρίς την εφαρμογή NAT(Network Address Translation). Οι υπηρεσίες των εφαρμογών του container γίνονται πλέον διαθέσιμες μέσω της IP του host στις θύρες τις οποίες κάνει EXPOSE το container. Συνεπώς, το port-mapping με το argument -p κατά τη δημιουργία του container(με χρήση του command run) παύει να έχει ισχύ.

* Overlay: Δημιουργεί ένα κατανεμημένο δίκτυο μεταξύ πολλαπλών docker deamon hosts. Το δίκτυο αυτό περιβάλλει το δίκτυο του κάθε host, δίνοντας έτσι τη δυνατότητα επικοινωνίας μεταξύ containers (που εν δυνάμει ανήκουν σε διαφορετικούς hosts) που είναι συνδεδεμένα σε αυτό. Η μεταφορά πακέτων-μηνυμάτων μεταξύ Docker daemon host και container παραλήπτη διεκπεραιώνεται με πλήρη διαφάνεια από το Docker, παρέχοντας επίσης την δυνατότητα για κρυπτογράφηση για την επίτευξη ασφάλειας. 

> [!INFORMATION]
> Ο Overlay Driver χρησιμοποιείται κυρίως για τη διασύνδεση πολλαπλών [υπηρεσιών Swarm][docker-swarm-service-link], ένας μηχανισμός που υπάγεται στο [Docker Swarm mode][docker-swarm-mode-link], το οποίο δεν καλύπτεται στο παρόν tutorial.  

Προκειμένου να κατασκευάσουμε ένα Docker δίκτυο αρκεί να εκτελέσουμε την εντολή:

```bash
docker network [network name]
```

Η δημιουργία και η ένταξη ενός container σε ένα συγκεκριμένο δίκτυο, πραγματοποιείται με την εκτέλεση της εντολής:

```bash
docker run -d --network [desired network name] --name [container name] [image name:tag]
```

Όλα τα networks που διαθέτει ο χρήστης στο σύστημά του μπορούν να εμφανιστούν με την εκτέλεση της εντολής:

```bash
docker network ls
```
ενώ η επισκόπηση των πληροφοριών ενός συγκεκριμένου network είναι εφικτή μέσω της εκτέλεσης της εντολής:

```bash
docker network inspect [network name]
```
Η σύνδεση ενός container σε ένα συγκεκριμένο network είναι εφικτή μέσω της εκτέλεσης της εντολής:

```bash
docker network connect [network name] [container name]
```
Η αποσύνδεση ενός container από ένα network είναι εφικτή μέσω της εκτέλεσης της εντολής:

```bash
docker network disconnect [network name] [container name]
```
Η διαγραφή ενός συγκεριμένου network, εφόσον δεν υπάρχει ενεργό container που να ανήκει σε αυτό, πραγματοποιείται με την εκτέλεση της εντολής:

```bash
docker network rm [network name]
```
Τέλος, η διαγραφή όλων των ανενεργών δικτύων του συστήματος πραγματοποιείται με την εκτέλεση της εντολής:

```bash
docker network prune
```
Η εντολή αυτή είναι χρήσιμη για τον καθαρισμό του συστήματός σας από δίκτυα που δεν χρησιμοποιούνται πλέον, εξοικονομώντας έτσι χώρο και πόρους.



# Contact

### Authors:

- Metaxakis Dimitris | <a href="mailto:d.metaxakis@ac.upatras.gr">d.metaxakis@ac.upatras.gr</a>
- Sofotasios Argiris | <a href="mailto:a.sofotasios@ac.upatras.gr">a.sofotasios@ac.upatras.gr</a>


# License

Distributed under the [MIT] License. See `LICENSE.md` for more details.


<!-- MARKDOWN LINKS & IMAGES -->
[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg
[license-link]: https://github.com/DmMeta/ChordSeek/blob/main/LICENSE
[windows-link]:https://docs.docker.com/desktop/install/windows-install/
[linux-link]: https://docs.docker.com/engine/install/ubuntu/
[macos-link]: https://docs.docker.com/desktop/install/mac-install/
[docker-rootless]: https://docs.docker.com/engine/security/rootless/
[dockerfile-cstd1]: ./case_studies/CaseStudy1/Dockerfile
[node-app]: ./case_studies/CaseStudy1/server.js
[docker-swarm-mode-link]: https://docs.docker.com/engine/swarm/
[docker-swarm-service-link]: https://docs.docker.com/engine/swarm/networking/