NAME := python-irc
RPMSPECDIR := .
RPMSPEC := $(RPMSPECDIR)/python-irc.spec
SOURCE := $(shell awk '/^Source0/{print $$NF}' < $(RPMSPEC))


clean:
	@echo "Cleaning up RPM building stuff"
	@rm -fR rpm-build results
	@echo "Cleaning up byte compiled python stuff"
	@find . -type f -regex ".*\.py[co]$$" -delete
	@echo "Cleaning up editor backup files"
	@find . -type f \( -name "*~" -or -name "#*" \) -delete
	@find . -type f \( -name "*.swp" \) -delete

deps:
	mkdir -p results
	@cd dependencies/ && ./build_deps.sh && cd ..
	@cp dependencies/results/*.rpm ./results

rpmcommon: clean deps
	@mkdir -p rpm-build
	@wget $(SOURCE) -O rpm-build/$(notdir $(SOURCE))

srpm: rpmcommon
	@rpmbuild --define "_topdir %(pwd)/rpm-build" \
	--define "_builddir %{_topdir}" \
	--define "_rpmdir %{_topdir}" \
	--define "_srcrpmdir %{_topdir}" \
	--define "_specdir $(RPMSPECDIR)" \
	--define "_sourcedir %{_topdir}" \
	-bs $(RPMSPEC)
	@echo "#############################################"
	@echo "$(NAME) SRPM is built:"
	@find rpm-build -maxdepth 2 -name '$(NAME)*src.rpm' | awk '{print "    " $$1}'
	@echo "#############################################"

rpm: rpmcommon
	@rpmbuild --define "_topdir %(pwd)/rpm-build" \
	--define "_builddir %{_topdir}" \
	--define "_rpmdir %{_topdir}" \
	--define "_srcrpmdir %{_topdir}" \
	--define "_specdir $(RPMSPECDIR)" \
	--define "_sourcedir %{_topdir}" \
	-ba $(RPMSPEC)
	@find rpm-build -name '*.rpm' -exec cp '{}' results/ \;
	@echo "#############################################"
	@echo "RPMs are built:"
	@find results -name '*.rpm' | sort
	@echo "#############################################"
