FROM ubuntu:latest

ENV PATH="/app:${PATH}"

RUN apt-get update && \
    apt install fortune-mod cowsay -y && \
    apt-get clean

WORKDIR /app

RUN cp /usr/games/cowsay /app/ && \
    cp /usr/games/fortune /app/

COPY wisecow.sh /app/wisecow.sh

RUN chmod +x /app/wisecow.sh

EXPOSE 4499

ENTRYPOINT ["/app/wisecow.sh"]
