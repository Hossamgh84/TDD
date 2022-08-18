# on peut pas mettre plus qu'un 127 constructions (commandes) 

FROM nomImage:tag

LABEL Version="1.0"

# parametres utilisés par docker lors la creation de l'image
ARG name="test"

# parametres utilisés par le container apres creation
ENV hostname="testhost"

# instructions à executer lors la creation de l'image
# ici normalement on fait les mises à jour et installations
RUN apt-get update && apt-get install -y curl

# copier un fichier par son chemin relatif à un dossier dans le container
COPY instructions_docker.txt /data/

# comme la commande copier avec la difference de la possibilité de decompresser un archive
ADD source dest

#preciser où à quel directory il faut realiser la prochaine commande
WORKDIR /the/workdir/path

# commande executer au demarage du conteneur qui sera creer à partir l'image
ENTRYPOINT [ "executable" ]

# commande au demmarrage de conteneur
CMD [ "ls && cd /data/ && mkdir new" ]

# ouvrir un port à la creation de conteneur
EXPOSE 8080

# lier un volume à mon conteneur
VOLUME [ "/var/log", "/var/lib/mysql" ]

# l'utilisateur par defaut du conteneur
USER user_Hossam