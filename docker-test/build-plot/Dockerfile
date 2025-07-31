FROM ubuntu:latest
RUN apt update
RUN apt install -y cron
RUN apt install -y exiftool
# install python
RUN apt-get update && apt-get install -y python3 python3-pip
# install matplot lib
RUN pip3 install matplotlib --break-system-packages
# install latex, otherwise matplot wont be able to save the plot
RUN apt-get install -y dvipng texlive-latex-extra texlive-fonts-recommended cm-super
COPY crontab /etc/cron.d/my-cron
RUN chmod 644 /etc/cron.d/my-cron
COPY plot.py /var/local
COPY makePlot.sh /var/local
COPY getMetadata.sh /var/local
# start the cron service after Building.
# (-f option) keep cronjob running in the foreground, Docker wont end container
ENTRYPOINT cron -f
