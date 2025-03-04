# VEHICLE SIGNAL SPECIFICATION

[![License](https://img.shields.io/badge/License-MPL%202.0-blue.svg)](https://opensource.org/license/MPL-2.0)
[![Build Status](https://github.com/COVESA/vehicle_signal_specification/actions/workflows/buildcheck.yml/badge.svg)](https://github.com/COVESA/vehicle_signal_specification/actions/workflows/buildcheck.yml?query=branch%3Amaster)

The overall goal of the Vehicle Signal Specification (VSS) is to create a common understanding of vehicle signals in order to reach a “common language” independent of the protocol or serialisation format.

Generated documentation from latest commit on master branch is available at: [Vehicle Signal Specification Documentation](https://covesa.github.io/vehicle_signal_specification/).

## Getting started

### Using VSS
To use a specific version of VSS in your toolchain, head over to our [releases page](https://github.com/COVESA/vehicle_signal_specification/releases/).
The latest official release can be found [here](https://github.com/COVESA/vehicle_signal_specification/releases/latest).

Work towards the next version is continuously ongoing in the [master branch](https://github.com/COVESA/vehicle_signal_specification/tree/master).
To work with the specification directly, you need to clone this repository.

For more information on how to set up the development environment and to be able to transform source *.vspec files to
other formats see our [build guideline document](BUILD.md) and documentation in [VSS-tools](https://github.com/COVESA/vss-tools/blob/master/README.md).

### Discuss all things VSS, "meet" the community

The community has regular calls to discuss topics around VSS.
This includes specific tickets in this repository as well as the broader direction in which VSS is evolving.
You can find current call coordinates and dates in [our wiki](https://github.com/COVESA/vehicle_signal_specification/wiki/Weekly-meeting#meeting).

### Contribute to VSS

For detailed information see our [contribution guide](CONTRIBUTING.md)!

### VSS version and release handling

Both VSS (this repository) and [VSS-tools](https://github.com/COVESA/vss-tools) use a [PEP](https://peps.python.org/pep-0440/)
inspired version scheme.

Version is visible in the [Vehicle.vspec](spec/Vehicle/Vehicle.vspec) file where `VersionVSS.Label` typically is
`-dev` for ongoing work in master-branch and an empty string for released versions.

Versions are tagged in the form `vX.Y(.Z)` and the same syntax is used as names for VSS releases.
VSS-tools is tagged but not released.
For release candidates the form `vX.YrcN` is used. The `rcN` suffix is not used in
[Vehicle.vspec](spec/Vehicle/Vehicle.vspec) files.

For more information on how versions are managed see the [Release Instruction](https://github.com/COVESA/vehicle_signal_specification/wiki/Release-Instructions-and-Checklist)

## Contributors
VSS is an open standard and we invite anybody to contribute. Currently VSS contains - among others - significant  contributions from
 - [Bayerische Motoren Werke Aktiengesellschaft (BMW AG)](https://www.bmwgroup.com/en.html)
 - [Volvo Cars](https://www.volvocars.com/)
 - [Jaguar Land Rover](https://www.jaguarlandrover.com/)
 - [Robert Bosch GmbH](https://www.bosch.com/)
 - [Geotab Inc](https://www.geotab.com/about/).
