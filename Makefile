PREFIX ?= /usr/local
SYSCONFDIR ?= $(PREFIX)/etc


all:

install:
	install -d $(DESTDIR)$(SYSCONFDIR)/rhsm/ca
	install -m 644 -p etc-conf/redhat-entitlement-authority.pem $(DESTDIR)$(SYSCONFDIR)/rhsm/ca/redhat-entitlement-authority.pem
	install -m 644 -p etc-conf/redhat-uep.pem $(DESTDIR)$(SYSCONFDIR)/rhsm/ca/redhat-uep.pem
