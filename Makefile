PREFIX ?= /usr/local
SYSCONFDIR ?= $(PREFIX)/etc


all: check

check:
	find etc-conf -name '*.pem' -print | xargs -t -I{} openssl x509 -in {} -noout -checkend 0

install:
	install -d $(DESTDIR)$(SYSCONFDIR)/rhsm/ca
	install -m 644 -p etc-conf/redhat-entitlement-authority.pem $(DESTDIR)$(SYSCONFDIR)/rhsm/ca/redhat-entitlement-authority.pem
	install -m 644 -p etc-conf/redhat-uep.pem $(DESTDIR)$(SYSCONFDIR)/rhsm/ca/redhat-uep.pem
