FROM node:18
RUN apt update && \
    apt install -y git build-essential cmake clang libssl-dev less man-db sudo cppcheck python3-pip gdb&& \
    chsh -s /bin/bash node
ARG USERNAME=node
RUN id -u $USERNAME 2>/dev/null || useradd -m $USERNAME && \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME
RUN sudo pip install --break-system-packages flawfinder lizard
WORKDIR /home/node/works
COPY . /home/node/works
