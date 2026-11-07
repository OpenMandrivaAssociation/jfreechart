Name:		jfreechart
Version:	1.5.6
Release:	1
Summary:	Chart library for Java
Group:		Development/Java
License:	LGPLv2+
URL:		https://www.jfree.org/jfreechart/
Source0:	https://github.com/jfree/jfreechart/archive/refs/tags/v%{version}.tar.gz#/jfreechart-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
# Provided scope. The servlet helpers are optional at runtime, and builddep skips that scope.
BuildRequires:	mvn(javax.servlet:javax.servlet-api)
# The published servlet POM parents jvnet-parent 3. The package does not require it.
# sysjar rewrites that parent to the installed jvnet-parent.
BuildRequires:	mvn(net.java:jvnet-parent:pom::)
BuildSystem:	maven
BuildOption(install):	--file-name jfreechart

Obsoletes:	%{name}-swt < %{version}-%{release}
Obsoletes:	%{name}-javadoc < %{version}-%{release}

%description
JFreeChart draws bar, pie, line, XY, time series, and Sankey charts
with Java2D. 1.5.6 requires Java 8. The classes that used to come
from JCommon are part of this jar. 1.5.6 adds SymbolAxis.setSymbols,
Crosshair label padding, and clearSeries methods on AbstractRenderer,
and fixes XYBarRenderer label fitting. The servlet helpers in
org.jfree.chart.servlet are deprecated upstream and stay in this jar.
The old SWT subpackage and the separate JavaFX extension are not
built. Tests are skipped. The automatic module name is
org.jfree.jfreechart.

%prep
%autosetup -n jfreechart-%{version}
python - <<'PY'
import xml.etree.ElementTree as ET
from pathlib import Path

NS = "http://maven.apache.org/POM/4.0.0"
ET.register_namespace("", NS)
tree = ET.parse("pom.xml")
root = tree.getroot()
parent_of = {child: parent for parent in root.iter() for child in list(parent)}
scope_tag = "{" + NS + "}scope"
art_tag = "{" + NS + "}artifactId"
ver_tag = "{" + NS + "}version"
removed = 0
rewritten = 0
for dep in list(root.iter("{" + NS + "}dependency")):
    scope = dep.find(scope_tag)
    if scope is not None and (scope.text or "") == "test":
        parent_of[dep].remove(dep)
        removed += 1
        continue
    art = dep.find(art_tag)
    if art is not None and art.text == "servlet-api":
        art.text = "javax.servlet-api"
        ver = dep.find(ver_tag)
        if ver is not None:
            ver.text = "4.0.1"
        rewritten += 1
if removed != 3 or rewritten != 1:
    raise SystemExit("dependency edit removed " + str(removed) + " rewritten " + str(rewritten))
tree.write("pom.xml", encoding="utf-8", xml_declaration=True)
text = Path("pom.xml").read_text(encoding="utf-8")
for needle in (
    "<artifactId>javax.servlet-api</artifactId>",
    "<version>4.0.1</version>",
    "<scope>provided</scope>",
    "<source>1.8</source>",
    "<target>1.8</target>",
    "Automatic-Module-Name",
    "org.jfree.jfreechart",
):
    if needle not in text:
        raise SystemExit("pom missing " + needle)
for needle in ("junit", "equalsverifier", "<artifactId>servlet-api</artifactId>", "<scope>test</scope>"):
    if needle in text:
        raise SystemExit("pom still contains " + needle)
files = list(Path("src/main/java").rglob("*.java"))
if len(files) != 658:
    raise SystemExit("unexpected java file count " + str(len(files)))
PY

%build -a
cat > manifest-addition <<'EOF'
Automatic-Module-Name: org.jfree.jfreechart
EOF
jar ufm target/jfreechart-%{version}.jar manifest-addition
java --module-path target/jfreechart-%{version}.jar --describe-module org.jfree.jfreechart > module-describe.txt
# A versioned jar prints "name@version ... automatic", not "name automatic".
grep -q '^org.jfree.jfreechart' module-describe.txt || { cat module-describe.txt; exit 1; }
grep -q ' automatic$' module-describe.txt || { cat module-describe.txt; exit 1; }

%files -f .mfiles
%doc README.md licence-LGPL.txt
