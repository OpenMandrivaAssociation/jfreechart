# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define gcj_support 0

%define section   free

%define jcommon_version 1.0.16

Name:             jfreechart
Version:          1.0.13
Release:          2
Summary:          Charts Generation library
License:          LGPLv2+
URL:              http://www.jfree.org/jfreechart/
Source0:          http://downloads.sourceforge.net/jfreechart/jfreechart-%{version}.tar.bz2
Patch0:           jfreechart-1.0.5-build_xml.patch
Patch1:           jfreechart-1.0.13-jarpath.patch
Group:            Development/Java
Requires:         jcommon >= 0:%{jcommon_version}
BuildRequires:    ant >= 0:1.6
BuildRequires:    ant-junit >= 0:1.6
BuildRequires:    jcommon >= 0:%{jcommon_version}
BuildRequires:    java-rpmbuild >= 0:1.6
BuildRequires:    junit
BuildRequires:    servlet
BuildRequires:    xml-commons-apis
BuildRequires:    itext
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
%endif

%description
Free Java class library for generating charts.

%package experimental
Summary:        Experimental components for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
%if %{gcj_support}
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description experimental
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:            Development/Java

%description javadoc
Javadoc for %{name}.

%description javadoc -l fr
Javadoc pour %{name}.

%prep
%setup -q
%remove_java_binaries
%patch0 -p0 -b .sav
%patch1 -p0

%build

%{ant} -f ant/build.xml \
   -Djunit.jar=$(build-classpath junit) \
   -Djcommon.jar=$(build-classpath jcommon) \
   -Dservlet.jar=$(build-classpath servlet) \
   -Dgnujaxp.jar=$(build-classpath xml-commons-apis) \
   -Ditext.jar=$(build-classpath itext) \
   -Dbuildstable=true -Dproject.outdir=. -Dbasedir=. \
   compile compile-experimental javadoc maven-bundle

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 lib/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
install -m 644 lib/%{name}-%{version}-experimental.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-experimental-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%{gcj_compile}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{gcj_support}
%post
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun
%{clean_gcjdb}
%endif

%if %{gcj_support}
%post experimental
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun experimental
%{clean_gcjdb}
%endif

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files experimental
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-experimental-%{version}.jar
%{_javadir}/%{name}-experimental.jar
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-experimental-%{version}.jar.*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}


%changelog
* Fri Aug 06 2010 Jerome Martin <jmartin@mandriva.org> 1.0.13-1mdv2011.0
+ Revision: 566699
- Version 1.0.13

* Fri Nov 27 2009 Jerome Martin <jmartin@mandriva.org> 1.0.11-0.0.3mdv2010.1
+ Revision: 470675
- rebuild

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.0.11-0.0.2mdv2010.0
+ Revision: 438029
- rebuild

* Mon Oct 20 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1.0.11-0.0.1mdv2009.1
+ Revision: 295815
- 1.0.11

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.0.10-2.0.1mdv2009.0
+ Revision: 267210
- rebuild early 2009.0 package (before pixel changes)

* Fri Jun 13 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1.0.10-0.0.1mdv2009.0
+ Revision: 218684
- new version 1.0.10 and disable gcj compile

* Mon Jan 21 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1.0.9-0.0.1mdv2008.1
+ Revision: 155775
- new version and spec cleanup

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Anssi Hannula <anssi@mandriva.org> 1.0.5-1.0.2mdv2008.1
+ Revision: 120939
- buildrequire java-rpmbuild, i.e. build with icedtea on x86(_64)

* Fri Sep 21 2007 David Walluck <walluck@mandriva.org> 1.0.5-1.0.1mdv2008.0
+ Revision: 91767
- enable gcj support
- fix release tag
- fix buildroot
- remove spurious gnu-crypto BR
- remove java-gcj-compat Requires
- remove jars, don't just move them
- don't build tests
- fix javadoc (no ghost, no post(un))
- fix gcj dir perms
- fix ant call

* Wed Sep 19 2007 Nicolas Vigier <nvigier@mandriva.com> 1.0.5-1mdv2008.0
+ Revision: 90967
- adapt to mandriva
- Import jfreechart



* Fri May 18 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.0.5-1jpp
- Upgrade to 1.0.5
- Make Vendor, Distribution based on macro
- Add gcj_support option
- No -demo subpackage, -experimental subpackage instead
- Activate tests

* Fri Apr 21 2006 Fernando Nasser <fnasser@redhat.com> - 0:0.9.21-3jpp
- Make demo subpackage optional

* Fri Apr 21 2006 Fernando Nasser <fnasser@redhat.com> - 0:0.9.21-2jpp
- First JPP 1.7 build

* Tue Sep 20 2005 Ralph Apel <r.apel at r-apel.de> - 0:0.9.21-1jpp
- Upgrade to 0.9.21 

* Thu Dec 02 2004 Ralph Apel <r.apel at r-apel.de> - 0:0.9.20-1jpp
- Upgrade to 0.9.20 (last version with -demo included, for jboss32)

* Sun Nov 14 2004 Ville Skyttä <scop at jpackage.org> - 0:0.9.16-3jpp
- Remove bogus batik dependency.

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0.9.16-2jpp
- Rebuild with ant-1.6.2

* Tue Feb 17 2004 Kaj J. Niemi <kajtzu@fi.basen.net> 0.9.16-1jpp
- 0.9.16

* Fri May 09 2003 David Walluck <david@anti-microsoft.org> 0:0.9.8-1jpp
- 0.9.8
- update for JPackage 1.5

* Fri Mar 11 2003 Henri Gomez <hgomez@users.sourceforge.net> 0.9.6-2jpp
- update spec to respect JPP 1.5 policy

* Tue Mar 08 2003 Henri Gomez <hgomez@users.sourceforge.net> 0.9.6-1jpp
- 0.9.6
- requires jcommon 0.7.2 min
- no more sub package test

* Mon Oct 28 2002 Henri Gomez <hgomez@users.sourceforge.net> 0.9.4-1jpp
- Initial release
