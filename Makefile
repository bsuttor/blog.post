#!/usr/bin/make
#
all: run
VERSION=`cat version.txt`

.PHONY: bootstrap
bootstrap:
	if ! test -f bin/python; then virtualenv-2.7 --no-site-packages .;fi
	if ! test -f buildout.cfg;then ln -s prod.cfg buildout.cfg;fi
	./bin/python bootstrap.py

.PHONY: buildout
buildout:
	if ! test -f bin/buildout;then make bootstrap;fi
	#if ! test -f var/filestorage/Data.fs;then make standard-config; else bin/buildout -Nt 7;fi
	bin/buildout -t 7

.PHONY: dev-install
dev-install:
	if ! test -f buildout.cfg;then ln -s dev.cfg buildout.cfg;fi
	make buildout

.PHONY: standard-config
standard-config:
	if ! test -f bin/buildout;then make bootstrap;fi
	bin/buildout -c standard-config.cfg

.PHONY: run
run:
	if ! test -f bin/instance1;then make buildout;fi
	bin/instance1 fg

.PHONY: cleanall
cleanall:
	rm -fr develop-eggs downloads eggs parts .installed.cfg lib include bin buildout.cfg .mr.developer.cfg

.PHONY: deb
deb:
	git-dch -a --ignore-branch
	dch -v $(VERSION).$(BUILD_NUMBER) release --no-auto-nmu
	dpkg-buildpackage -b -uc -us


.PHONY: mrbob
mrbob:
	./bin/pip install -i http://pypi.imio.be/imio/imio/+simple/ bobtemplates.imio
	echo "[variables]" > debian.ini
	echo "debian.name = website" >> debian.ini
	./bin/mrbob -c debian.ini -O debian bobtemplates:debian
