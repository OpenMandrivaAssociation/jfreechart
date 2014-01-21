%{?_javapackages_macros:%_javapackages_macros}
# want the fedora extensions...
%global fedora 20
# TODO: junit QA tests

Name:           jfreechart
Version:        1.0.14
Release:        10.1%{?dist}
Summary:        Java chart library


License:        LGPLv2+
URL:            http://www.jfree.org/jfreechart/
Source0:        http://download.sourceforge.net/sourceforge/jfreechart/%{name}-%{version}.tar.gz
Source1:        bnd.properties

Requires:       servlet java jpackage-utils
Requires:       jcommon >= 1.0.17
BuildRequires:  %{requires} ant java-devel servlet
%if 0%{?fedora}
BuildRequires:  eclipse-swt
%endif
# Required for converting jars to OSGi bundles
BuildRequires:  aqute-bnd

BuildArch:      noarch
Patch0:         remove_itext_dep.patch

%description
JFreeChart is a free 100% Java chart library that makes it easy for
developers to display professional quality charts in their applications.

%if 0%{?fedora}
%package swt
Summary:        Experimental swt extension for jfreechart

Requires:       %{name} = %{version}-%{release}
Requires:       eclipse-swt jpackage-utils

%description swt
Experimental swt extension for jfreechart.
%endif

%package javadoc
Summary:        Javadocs for %{name}

Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
# Erase prebuilt files
find \( -name '*.jar' -o -name '*.class' \) -exec rm -f '{}' \;
%patch0

%build
CLASSPATH=$(build-classpath jcommon servlet) \
        ant -f ant/build.xml \
        compile javadoc
%if 0%{?fedora}
# See RHBZ#912664. There seems to be some dispute about build-classpath.
# So don't use it for swt.
ant -f ant/build-swt.xml \
        -Dswt.jar=%{_libdir}/eclipse/swt.jar \
        -Djcommon.jar=$(build-classpath jcommon) \
        -Djfreechart.jar=lib/jfreechart-%{version}.jar
%endif
# Convert to OSGi bundle
java -Djfreechart.bundle.version="%{version}" -jar $(build-classpath aqute-bnd) \
   wrap -output lib/%{name}-%{version}.bar -properties %{SOURCE1} lib/%{name}-%{version}.jar

%install
# Directory structure
install -d $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d $RPM_BUILD_ROOT%{_mavenpomdir}

# JARs and JavaDoc
install -m 644 lib/jfreechart-%{version}.bar  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}.jar
%if 0%{?fedora}
install -m 644 lib/swtgraphics2d.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}/swtgraphics2d.jar
install -m 644 lib/jfreechart-%{version}-swt.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-swt.jar
%endif
cp -rp javadoc/. $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}.jar
%doc ChangeLog licence-LGPL.txt NEWS README.txt

%if 0%{?fedora}
%files swt
%{_javadir}/%{name}/swtgraphics2d*.jar
%{_javadir}/%{name}/%{name}-swt*.jar
%endif

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-9
- Fix FTBFS due to build-classpath not finding swt.jar any
  longer. See RHBZ#912664.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-7
- Remove itext dependency in pom.

* Fri Nov 16 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-6
- Conditionally build jfreechart-swt.

* Mon Sep 17 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-4
- Set proper Bundle-{Version,SymbolicName,Name} in manifest.

* Tue Jul 24 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-3
- Add aqute bnd instructions so as to produce OSGi metadata.
- Based on kdaniel's suggestion, use build-classpath script to find swt

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Alexander Kurtakov <akurtako@redhat.com> 1.0.14-1
- Update to new upstream version 1.0.14.
- Use pom.xml file from the tarball.

* Wed Feb 15 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.13-5
- Added Maven POM: BZ#789586

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0.13-3
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 19 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.0.13-1
- Update to a later release
- Cosmetic fixes

* Mon Apr 19 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.0.10-4
- Enable SWT support (ELMORABITY Mohamed, #583339)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jul 19 2008 Lubomir Rintel (Fedora Astronomy) <lkundrak@fedoraproject.org> - 1.0.10-1
- Initial packaging
