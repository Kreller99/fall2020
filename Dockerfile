#Base image
FROM sphinxdoc/sphinx

# Arguments for github authendication
ARG token
ARG user
ARG repo

# setup working/start dir
WORKDIR /docs
COPY .gitconfig ../root/.gitconfig 


# pip installations of sphix dependencies
# theme, javascript extensions, and markdown converter
RUN pip3 install sphinx_rtd_theme
RUN pip3 install nbsphinx
RUN pip3 install recommonmark

# install pandoc and git in the image
RUN apt-get update \
 && apt-get install -y \
      pandoc \
      git \
 && apt-get autoremove \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# set up authendication for your github account
# token, user, repo arguments should be set at container creation time
RUN git clone https://$token:x-oauth-basic@github.com/$user/$repo.git
