# anatomy.md

> Auto-maintained by OpenWolf. Last scanned: 2026-07-09T21:06:57.784Z
> Files: 490 tracked | Anatomy hits: 0 | Misses: 0

## ./

- `.agent-config.toml` (~14 tok)
- `.DS_Store` (~1639 tok)
- `.gitignore` — Git ignore rules (~23 tok)
- `CLAUDE.md` — OpenWolf (~66 tok)
- `env.local` (~67 tok)
- `GEMINI.md` (~9 tok)
- `main.py` (~393 tok)
- `POLISH-SPEC.md` — TidyEmail -- Polish Spec (Open-Source Revival) (~1640 tok)
- `PREMORTEM.md` — TidyEmail -- Premortem (Failure-Modes-as-Gates) (~933 tok)
- `README.md` — Project documentation (~347 tok)
- `rules.example.toml` — TidyEmail rules -- authored once by `tidyemail init`, then run deterministically. (~303 tok)
- `run.sh` (~35 tok)
- `tidyemail.code-workspace` (~16 tok)

## .claude/

- `settings.json` (~441 tok)

## .claude/rules/

- `openwolf.md` (~313 tok)

## .devcontainer/

- `.dockerignore` — Docker ignore rules (~6 tok)
- `devcontainer.json` (~115 tok)
- `Dockerfile` — Docker container definition (~167 tok)

## .github/

- `CODEOWNERS` — All files — Esturban reviews every PR (~14 tok)
- `copilot_instructions.md` (~125 tok)
- `pull_request_template.md` — What (~80 tok)

## .github/workflows/

- `ci.yml` — CI: CI (~306 tok)
- `dev-to-trunk.yml` — CI: Dev to Trunk Auto-PR (~983 tok)
- `pr-to-prod.yml` — CI: 'tidyemail to prod' (~342 tok)
- `release.yml` — CI: Release (~220 tok)

## data/

- `academic.json` (~13 tok)
- `bids.json` (~58 tok)
- `bills.json` (~44 tok)
- `development.json` (~155 tok)
- `domains.json` (~1333 tok)
- `important.json` (~449 tok)
- `job_boards.json` (~210 tok)

## examples/

- `1_mark_as_read.py` — Add the parent directory to the Python path (~452 tok)
- `2_categorize_emails_1_folder.py` — Add the parent directory to the Python path (~489 tok)
- `3_categorize_emails_multiple_folders.py` — Add the parent directory to the Python path (~571 tok)

## tidyemail/

- `__init__.py` (~42 tok)
- `utils.py` — for: connect_to_imap_server, fetch_emails, mark_emails_as_read, fetch_and_mark_emails + 3 more (~2476 tok)

## venv/

- `.DS_Store` (~1638 tok)
- `.gitignore` — Git ignore rules (~19 tok)
- `pyvenv.cfg` (~90 tok)

## venv/bin/

- `activate` — This file must be used with "source bin/activate" *from bash* (~572 tok)
- `activate.csh` — This file must be used with "source bin/activate.csh" *from csh*. (~254 tok)
- `activate.fish` — This file must be used with "source <venv>/bin/activate.fish" *from fish* (~595 tok)
- `Activate.ps1` — Declares from (~2409 tok)
- `dotenv` — -*- coding: utf-8 -*- (~74 tok)
- `pip` — -*- coding: utf-8 -*- (~76 tok)
- `pip3` — -*- coding: utf-8 -*- (~76 tok)
- `pip3.13` — -*- coding: utf-8 -*- (~76 tok)

## venv/lib/python3.13/site-packages/dotenv/

- `__init__.py` — load_ipython_extension, get_cli_string (~370 tok)
- `__main__.py` — Entry point for cli, enables execution with `python -m dotenv` (~37 tok)
- `cli.py` — enumerate_env, cli, stream_file, list + 5 more (~1660 tok)
- `ipython.py` — class: dotenv, load_ipython_extension (~373 tok)
- `main.py` — View: get (~3457 tok)
- `parser.py` — Original: make_regex, start, set, advance + 13 more (~1482 tok)
- `py.typed` — Marker file for PEP 561 (~7 tok)
- `variables.py` — Atom: resolve, resolve, resolve, parse_variables (~671 tok)
- `version.py` (~7 tok)

## venv/lib/python3.13/site-packages/pip-24.2.dist-info/

- `AUTHORS.txt` (~2696 tok)
- `entry_points.txt` (~22 tok)
- `INSTALLER` (~2 tok)
- `LICENSE.txt` (~274 tok)
- `METADATA` (~967 tok)
- `RECORD` (~17488 tok)
- `REQUESTED` (~0 tok)
- `top_level.txt` (~1 tok)
- `WHEEL` (~25 tok)

## venv/lib/python3.13/site-packages/pip/

- `__init__.py` — main (~102 tok)
- `__main__.py` — Remove '' and current working directory from the first entry (~244 tok)
- `__pip-runner__.py` — Execute exactly this copy of pip, within a different environment. (~415 tok)
- `py.typed` (~77 tok)

## venv/lib/python3.13/site-packages/pip/_internal/

- `__init__.py` — init_logging() must be called before any call to logging.getLogger() (~147 tok)
- `build_env.py` — Build Environment used for isolation during sdist building (~2978 tok)
- `cache.py` — Cache Management (~2963 tok)
- `configuration.py` — Configuration management setup (~4002 tok)
- `exceptions.py` — Exceptions used throughout package. (~7247 tok)
- `main.py` — main (~98 tok)
- `pyproject.py` — URL configuration (~2082 tok)
- `self_outdated_check.py` — View: get (~2328 tok)
- `wheel_builder.py` — Orchestrator for building wheels from InstallRequirements. (~3372 tok)

## venv/lib/python3.13/site-packages/pip/_internal/cli/

- `__init__.py` — Subpackage containing all of pip's command line interface related code (~38 tok)
- `autocompletion.py` — Logic that powers autocompletion installed by ``pip completion``. (~1962 tok)
- `base_command.py` — Base Command class, and related routines (~2369 tok)
- `cmdoptions.py` — URL configuration (~8603 tok)
- `command_context.py` — CommandContextMixIn: main_context, enter_context (~222 tok)
- `index_command.py` — SessionCommandMixin: get_default_session, handle_pip_version_check (~1610 tok)
- `main_parser.py` — A single place for constructing and exposing the main parser (~1240 tok)
- `main.py` — Primary application entrypoint. (~805 tok)
- `parser.py` — Base option parser setup (~3089 tok)
- `progress_bars.py` — SQLAlchemy model (~776 tok)
- `req_command.py` — Contains the RequirementCommand base class. (~3500 tok)
- `spinners.py` — SpinnerInterface: spin, finish, spin, finish + 6 more (~1463 tok)
- `status_codes.py` (~34 tok)

## venv/lib/python3.13/site-packages/pip/_internal/commands/

- `__init__.py` — with: create_command, get_similar_commands (~1110 tok)
- `cache.py` — URL configuration (~2270 tok)
- `check.py` — CheckCommand: run (~648 tok)
- `completion.py` — CompletionCommand: add_options, run (~1225 tok)
- `configuration.py` — ConfigurationCommand: add_options, run, list_values, get_name + 6 more (~2791 tok)
- `debug.py` — DebugCommand: show_value, show_sys_implementation, create_vendor_txt_map, get_module_from_module_name + 7 more (~1942 tok)
- `download.py` — URL configuration (~1507 tok)
- `freeze.py` — URL configuration (~916 tok)
- `hash.py` — HashCommand: add_options, run (~487 tok)
- `help.py` — HelpCommand: run (~324 tok)
- `index.py` — IndexCommand: add_options, run, get_available_package_versions (~1352 tok)
- `inspect.py` — URL configuration (~912 tok)
- `install.py` — URL configuration (~8408 tok)
- `list.py` — URL configuration (~3649 tok)
- `search.py` — TransformedHit: add_options, run, search, transform_hits + 3 more (~1608 tok)
- `show.py` — ShowCommand: add_options, run, search_packages_info, print_results (~2145 tok)
- `uninstall.py` — UninstallCommand: add_options, run (~1112 tok)
- `wheel.py` — URL configuration (~1833 tok)

## venv/lib/python3.13/site-packages/pip/_internal/distributions/

- `__init__.py` — make_distribution_for_install_requirement (~246 tok)
- `base.py` — AbstractDistribution: build_tracker_id, get_metadata_distribution, prepare_distribution_metadata (~510 tok)
- `installed.py` — InstalledDistribution: build_tracker_id, get_metadata_distribution, prepare_distribution_metadata (~241 tok)
- `sdist.py` — SourceDistribution: build_tracker_id, get_metadata_distribution, prepare_distribution_metadata (~1929 tok)
- `wheel.py` — WheelDistribution: build_tracker_id, get_metadata_distribution, prepare_distribution_metadata (~377 tok)

## venv/lib/python3.13/site-packages/pip/_internal/index/

- `__init__.py` — Index interaction code (~9 tok)
- `collector.py` — from: with_cached_index_content, wrapper, wrapper_wrapper, parse_links + 2 more (~4648 tok)
- `package_finder.py` — Routines related to PyPI, indexes (~10762 tok)
- `sources.py` — URL configuration (~2483 tok)

## venv/lib/python3.13/site-packages/pip/_internal/locations/

- `__init__.py` — URL configuration (~4265 tok)
- `_distutils.py` — Locations where we look for configs, install stuff, etc (~1717 tok)
- `_sysconfig.py` — get_scheme, get_bin_prefix, get_purelib, get_platlib (~2207 tok)
- `base.py` — Application Directories (~731 tok)

## venv/lib/python3.13/site-packages/pip/_internal/metadata/

- `__init__.py` — Backend: select_backend, get_default_environment, get_environment, get_directory_distribution + 2 more (~1240 tok)
- `_json.py` — Extracted from https://github.com/pfmoore/pkg_metadata (~756 tok)
- `base.py` — URL configuration (~7228 tok)
- `pkg_resources.py` — URL configuration (~3012 tok)

## venv/lib/python3.13/site-packages/pip/_internal/metadata/importlib/

- `__init__.py` (~39 tok)
- `_compat.py` — BadMetadata: name, parent, get_info_location, parse_name_and_version_from_info_directory + 1 more (~799 tok)
- `_dists.py` — URL patterns: 1 routes (~2291 tok)
- `_envs.py` — URL configuration (~2124 tok)

## venv/lib/python3.13/site-packages/pip/_internal/models/

- `__init__.py` — A package that contains models that represent entities. (~18 tok)
- `candidate.py` — Declares from (~216 tok)
- `direct_url.py` — PEP 610 (~1880 tok)
- `format_control.py` — FormatControl: handle_mutual_excludes, get_allowed_formats, disallow_binaries (~711 tok)
- `index.py` — URL patterns: 2 routes (~295 tok)
- `installation_report.py` — InstallationReport: to_dict (~806 tok)
- `link.py` — URL configuration (~6010 tok)
- `scheme.py` — Declares SCHEME_KEYS (~165 tok)
- `search_scope.py` — URL configuration (~1295 tok)
- `selection_prefs.py` — TODO: This needs Python 3.10's improved slots support for dataclasses (~576 tok)
- `target_python.py` — TargetPython: format_given, get_sorted_tags, get_unsorted_tags (~1221 tok)
- `wheel.py` — Represents a wheel file and provides access to the various parts of the (~1029 tok)

## venv/lib/python3.13/site-packages/pip/_internal/network/

- `__init__.py` — Contains purely network-related utilities. (~15 tok)
- `auth.py` — Network Authentication Helpers (~5946 tok)
- `cache.py` — HTTP cache implementation. (~1125 tok)
- `download.py` — Download files with progress indicators. (~1728 tok)
- `lazy_wheel.py` — Lazy ZIP over HTTP (~2183 tok)
- `session.py` — PipSession and supporting code, containing all pip-specific (~5355 tok)
- `utils.py` — The following comments and HTTP headers were originally added by (~1168 tok)
- `xmlrpc.py` — xmlrpclib.Transport implementation (~526 tok)

## venv/lib/python3.13/site-packages/pip/_internal/operations/

- `__init__.py` (~0 tok)
- `check.py` — Validation of dependencies of packages (~1690 tok)
- `freeze.py` — URL configuration (~2819 tok)
- `prepare.py` — Prepares a distribution for installation (~8034 tok)

## venv/lib/python3.13/site-packages/pip/_internal/operations/install/

- `__init__.py` — For modules related to installing packages. (~15 tok)
- `editable_legacy.py` — Legacy editable installation process, i.e. `setup.py develop`. (~367 tok)
- `wheel.py` — Support for installing and building the "wheel" binary package format. (~7890 tok)

## venv/lib/python3.13/site-packages/pip/_internal/req/

- `__init__.py` — from: install_given_reqs (~758 tok)
- `constructors.py` — Backing implementation for InstallRequirement's various constructors (~5264 tok)
- `req_file.py` — URL configuration (~5054 tok)
- `req_install.py` — URL configuration (~10226 tok)
- `req_set.py` — RequirementSet: add_unnamed_requirement, add_named_requirement, has_requirement, get_requirement + 2 more (~817 tok)
- `req_uninstall.py` — URL configuration (~6816 tok)

## venv/lib/python3.13/site-packages/pip/_internal/resolution/

- `__init__.py` (~0 tok)
- `base.py` — BaseResolver: resolve, get_installation_order (~167 tok)

## venv/lib/python3.13/site-packages/pip/_internal/resolution/legacy/

- `__init__.py` (~0 tok)
- `resolver.py` — Dependency Resolution (~6877 tok)

## venv/lib/python3.13/site-packages/pip/_internal/resolution/resolvelib/

- `__init__.py` (~0 tok)
- `base.py` — from: format_name, empty, from_ireq, is_satisfied_by + 14 more (~1436 tok)
- `candidates.py` — _InstallRequirementBackedCandidate: as_base_candidate, make_install_req_from_link, make_install_req_from_editable, source_link + 6 more (~5664 tok)
- `factory.py` — ConflictCause: force_reinstall, iter_index_candidate_infos, is_pinned (~9274 tok)
- `found_candidates.py` — Utilities to lazily create and visit candidates found. (~1824 tok)
- `provider.py` — PipProvider: identify, get_preference, find_matches, is_satisfied_by + 2 more (~2839 tok)
- `reporter.py` — PipReporter: rejecting_candidate, starting, starting_round, ending_round + 4 more (~906 tok)
- `requirements.py` — ExplicitRequirement: project_name, name, format_for_error, get_candidate_lookup + 16 more (~2305 tok)
- `resolver.py` — Resolver: resolve, get_installation_order, get_topological_weights, visit (~3598 tok)

## venv/lib/python3.13/site-packages/pip/_internal/utils/

- `__init__.py` (~0 tok)
- `_jaraco_text.py` — Functions brought over from jaraco.text. (~958 tok)
- `_log.py` — Customize logging (~290 tok)
- `appdirs.py` — user_cache_dir, user_config_dir, site_config_dirs (~476 tok)
- `compat.py` — Stuff that differs in different Python versions and platform (~686 tok)
- `compatibility_tags.py` — Generate and work with PEP 425 Compatibility Tags. (~1537 tok)
- `datetime.py` — For when pip wants to check the date or time. (~70 tok)
- `deprecation.py` — PipDeprecationWarning: install_warning_logger, deprecated (~1060 tok)
- `direct_url_helpers.py` — direct_url_as_pep440_direct_reference, direct_url_for_editable, direct_url_from_link (~914 tok)
- `egg_link.py` — URL configuration (~704 tok)
- `encoding.py` — auto_decode (~334 tok)
- `entrypoints.py` — get_best_invocation_for_this_pip, get_best_invocation_for_this_python (~876 tok)
- `filesystem.py` — check_path_owner, adjacent_tmp_file, test_writable_dir, find_files + 4 more (~1415 tok)
- `filetypes.py` — Filetype information. (~205 tok)
- `glibc.py` — glibc_version_string, glibc_version_string_confstr, glibc_version_string_ctypes, libc_ver (~1067 tok)
- `hashes.py` — URL configuration (~1421 tok)
- `logging.py` — from: indent_log, get_indentation, get_message_start, format + 5 more (~3316 tok)
- `misc.py` — URL configuration (~6785 tok)
- `packaging.py` — check_requires_python, get_requirement, safe_extra (~603 tok)
- `retry.py` — retry, wrapper, retry_wrapped (~398 tok)
- `setuptools_build.py` — Shim to wrap setup.py invocation with setuptools (~1268 tok)
- `subprocess.py` — make_command, format_command_args, reveal_command_args, call_subprocess + 2 more (~2568 tok)
- `temp_dir.py` — URL configuration (~2660 tok)
- `unpacking.py` — Utilities related archives. (~3415 tok)
- `urls.py` — URL configuration (~457 tok)
- `virtualenv.py` — URL configuration (~988 tok)
- `wheel.py` — Support functions for working with wheel files. (~1284 tok)

## venv/lib/python3.13/site-packages/pip/_internal/vcs/

- `__init__.py` — Expose a limited set of classes and functions so callers outside of (~171 tok)
- `bazaar.py` — URL configuration (~1008 tok)
- `git.py` — URL configuration (~5194 tok)
- `mercurial.py` — URL configuration (~1500 tok)
- `subversion.py` — URL configuration (~3353 tok)
- `versioncontrol.py` — Handles all VCS (version control) support (~6412 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/

- `__init__.py` — URL configuration (~1393 tok)
- `typing_extensions.py` — _Sentinel: final, done, done, IntVar + 10 more (~38429 tok)
- `vendor.txt` (~83 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/cachecontrol/

- `__init__.py` — CacheControl import Interface. (~194 tok)
- `_cmd.py` — SPDX-FileCopyrightText: 2015 Eric Larson (~497 tok)
- `adapter.py` — SPDX-FileCopyrightText: 2015 Eric Larson (~1816 tok)
- `cache.py` — SPDX-FileCopyrightText: 2015 Eric Larson (~558 tok)
- `controller.py` — SPDX-FileCopyrightText: 2015 Eric Larson (~5308 tok)
- `filewrapper.py` — SPDX-FileCopyrightText: 2015 Eric Larson (~1227 tok)
- `heuristics.py` — SPDX-FileCopyrightText: 2015 Eric Larson (~1382 tok)
- `py.typed` (~0 tok)
- `serialize.py` — SPDX-FileCopyrightText: 2015 Eric Larson (~1476 tok)
- `wrapper.py` — SPDX-FileCopyrightText: 2015 Eric Larson (~405 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/cachecontrol/caches/

- `__init__.py` — SPDX-FileCopyrightText: 2015 Eric Larson (~87 tok)
- `file_cache.py` — SPDX-FileCopyrightText: 2015 Eric Larson (~1545 tok)
- `redis_cache.py` — SPDX-FileCopyrightText: 2015 Eric Larson (~396 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/certifi/

- `__init__.py` (~27 tok)
- `__main__.py` (~73 tok)
- `cacert.pem` — Issuer: CN=GlobalSign Root CA O=GlobalSign nv-sa OU=Root CA (~77741 tok)
- `core.py` — URL patterns: 3 routes (~1282 tok)
- `py.typed` (~0 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/distlib/

- `__init__.py` — -*- coding: utf-8 -*- (~179 tok)
- `compat.py` — -*- coding: utf-8 -*- (~11853 tok)
- `database.py` — PEP 376 implementation. (~14848 tok)
- `index.py` — -*- coding: utf-8 -*- (~5942 tok)
- `locators.py` — -*- coding: utf-8 -*- (~14791 tok)
- `manifest.py` — -*- coding: utf-8 -*- (~4048 tok)
- `markers.py` — -*- coding: utf-8 -*- (~1506 tok)
- `metadata.py` — Implementation of the Metadata for Python packages PEPs. (~11341 tok)
- `resources.py` — -*- coding: utf-8 -*- (~3092 tok)
- `scripts.py` — -*- coding: utf-8 -*- (~5365 tok)
- `util.py` — See LICENSE.txt and CONTRIBUTORS.txt. (~19295 tok)
- `version.py` — -*- coding: utf-8 -*- (~6785 tok)
- `wheel.py` — -*- coding: utf-8 -*- (~12560 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/distro/

- `__init__.py` (~281 tok)
- `__main__.py` (~19 tok)
- `distro.py` — you may not use this file except in compliance with the License. (~14123 tok)
- `py.typed` (~0 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/idna/

- `__init__.py` (~243 tok)
- `codec.py` — Codec: encode, decode, search_function (~979 tok)
- `compat.py` — ToASCII, ToUnicode, nameprep (~92 tok)
- `core.py` — IDNAError: valid_label_length, valid_string_length, check_bidi, check_initial_combiner + 10 more (~3618 tok)
- `idnadata.py` — This file is automatically generated by tools/idna-data (~22378 tok)
- `intranges.py` — intranges_from_list, intranges_contain (~538 tok)
- `package_data.py` (~6 tok)
- `py.typed` (~0 tok)
- `uts46data.py` — This file is automatically generated by tools/idna-data (~56467 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/msgpack/

- `__init__.py` — pack, packb, unpack (~308 tok)
- `exceptions.py` — Declares UnpackException (~309 tok)
- `ext.py` — ExtType: from_bytes, to_bytes, from_unix, to_unix + 4 more (~1609 tok)
- `fallback.py` — Fallback pure Python implementation of msgpack (~9479 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/packaging/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~142 tok)
- `_elffile.py` — ELFInvalid: interpreter (~938 tok)
- `_manylinux.py` — _GLibCVersion: platform_tags (~2739 tok)
- `_musllinux.py` — PEP 656 support. (~770 tok)
- `_parser.py` — Handwritten parser of dependency specifiers. (~2925 tok)
- `_structures.py` — This file is dual licensed under the terms of the Apache License, Version (~409 tok)
- `_tokenizer.py` — from: consume, check, expect, read + 2 more (~1507 tok)
- `markers.py` — This file is dual licensed under the terms of the Apache License, Version (~3049 tok)
- `metadata.py` — ExceptionGroup: parse_email (~9243 tok)
- `py.typed` (~0 tok)
- `requirements.py` — This file is dual licensed under the terms of the Apache License, Version (~842 tok)
- `specifiers.py` — This file is dual licensed under the terms of the Apache License, Version (~11354 tok)
- `tags.py` — This file is dual licensed under the terms of the Apache License, Version (~5396 tok)
- `utils.py` — This file is dual licensed under the terms of the Apache License, Version (~1511 tok)
- `version.py` — This file is dual licensed under the terms of the Apache License, Version (~4632 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/pkg_resources/

- `__init__.py` — TODO: Add Generic type annotations to initialized collections. (~35561 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/platformdirs/

- `__init__.py` — URL configuration (~6368 tok)
- `__main__.py` — Main entry point. (~430 tok)
- `android.py` — Android. (~2576 tok)
- `api.py` — Base API. (~2571 tok)
- `macos.py` — macOS. (~1595 tok)
- `py.typed` (~0 tok)
- `unix.py` — Unix. (~3041 tok)
- `version.py` — file generated by setuptools_scm (~118 tok)
- `windows.py` — Windows. (~2893 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/pygments/

- `__init__.py` — lex, format, highlight (~853 tok)
- `__main__.py` (~101 tok)
- `cmdline.py` — from: main_inner, is_only_option (~6759 tok)
- `console.py` — reset_color, colorize, ansiformat (~491 tok)
- `filter.py` — Filter: apply_filters, simplefilter, lowercase, filter + 1 more (~546 tok)
- `formatter.py` — Formatter: get_style_defs, format (~1255 tok)
- `lexer.py` — LexerMeta: add_filter, analyse_text, get_tokens, streamer + 2 more (~10100 tok)
- `modeline.py` — get_filetype_from_line, get_filetype_from_buffer (~288 tok)
- `plugin.py` — iter_entry_points, find_plugin_lexers, find_plugin_formatters, find_plugin_styles + 1 more (~541 tok)
- `regexopt.py` — make_charset, regex_opt_inner, regex_opt (~878 tok)
- `scanner.py` — EndOfText: eos, check, test, scan + 1 more (~884 tok)
- `sphinxext.py` — PygmentsDoc: run, document_lexers_overview, format_link, write_row + 5 more (~2281 tok)
- `style.py` — StyleMeta: colorformat, or, for, in + 3 more (~1835 tok)
- `token.py` — _TokenType: split, is_token_subtype, string_to_tokentype (~1779 tok)
- `unistring.py` (~18060 tok)
- `util.py` — View: get (~2866 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/pygments/filters/

- `__init__.py` — CodeTagFilter: find_filter_class, get_filter_by_name, get_all_filters, filter (~11539 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/pygments/formatters/

- `__init__.py` — that: get_all_formatters, find_formatter_class, get_formatter_by_name, load_formatter_from_file + 1 more (~1539 tok)
- `_mapping.py` — Automatically generated by scripts/gen_mapfiles.py. (~1194 tok)
- `bbcode.py` — BBCodeFormatter: in, format_unencoded (~949 tok)
- `groff.py` — GroffFormatter: in, in, format_unencoded (~1459 tok)
- `html.py` — HtmlFormatter: escape_html, webify (~10192 tok)
- `img.py` — URL configuration (~6654 tok)
- `irc.py` — IRCFormatter: ircformat, format_unencoded (~1424 tok)
- `latex.py` — LatexFormatter: escape_tex, rgbcolor, in, def + 1 more (~5516 tok)
- `other.py` — NullFormatter: format, format, write, flush + 2 more (~1439 tok)
- `pangomarkup.py` — PangoMarkupFormatter: escape_special_chars, format_unencoded (~634 tok)
- `rtf.py` — RtfFormatter: hex_to_rtf_color, format_unencoded (~3417 tok)
- `svg.py` — SvgFormatter: escape_html, format_unencoded (~2050 tok)
- `terminal.py` — TerminalFormatter: format, format_unencoded (~1336 tok)
- `terminal256.py` — EscapeSequence: escape, color_string, true_color_string, reset_string + 4 more (~3358 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/pygments/lexers/

- `__init__.py` — that: get_all_lexers, find_lexer_class, find_lexer_class_by_name, get_lexer_by_name + 8 more (~3462 tok)
- `_mapping.py` — Automatically generated by scripts/gen_mapfiles.py. (~21741 tok)
- `python.py` — PythonLexer: innerstring_rules, fstring_rules (~15340 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/pygments/styles/

- `__init__.py` — by: get_style_by_name, get_all_styles (~584 tok)
- `_mapping.py` — Automatically generated by scripts/gen_mapfiles.py. (~947 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/pyproject_hooks/

- `__init__.py` — Wrappers to call pyproject.toml-based build backend hooks. (~141 tok)
- `_compat.py` (~40 tok)
- `_impl.py` — URL configuration (~3406 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/pyproject_hooks/_in_process/

- `__init__.py` — This is a subpackage because the directory is on sys.path for _in_process.py (~156 tok)
- `_in_process.py` — This is invoked in a subprocess to call the build backend hooks. (~3122 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/requests/

- `__init__.py` — /__)  _  _     _   _ _/   _ (~1445 tok)
- `__version__.py` — .-. .-. .-. . . .-. .-. .-. .-. (~125 tok)
- `_internal_utils.py` — to_native_string, unicode_is_ascii (~428 tok)
- `adapters.py` — BaseAdapter: SOCKSProxyManager, send, close, init_poolmanager + 2 more (~7888 tok)
- `api.py` — request, get, options, head + 4 more (~1843 tok)
- `auth.py` — AuthBase: init_per_thread_state, build_digest_header, md5_utf8, sha_utf8 + 4 more (~2911 tok)
- `certs.py` — where (~164 tok)
- `compat.py` (~425 tok)
- `cookies.py` — View: get, update (~5312 tok)
- `exceptions.py` — Declares RequestException (~1221 tok)
- `help.py` — Module containing bug report helper(s). (~1090 tok)
- `hooks.py` — default_hooks, dispatch_hook (~210 tok)
- `models.py` — RequestEncodingMixin: path_url, register_hook, deregister_hook, prepare + 3 more (~10138 tok)
- `packages.py` — This code exists for backwards compatibility reasons. (~302 tok)
- `sessions.py` — SessionRedirectMixin: merge_setting, merge_hooks, get_redirect_target, should_strip_auth + 3 more (~8713 tok)
- `status_codes.py` — doc (~1234 tok)
- `structures.py` — View: get (~832 tok)
- `utils.py` — proxy_bypass_registry, proxy_bypass, dict_to_sequence, super_len + 7 more (~9609 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/resolvelib/

- `__init__.py` (~154 tok)
- `providers.py` — AbstractProvider: identify, get_preference, find_matches, is_satisfied_by + 2 more (~1678 tok)
- `py.typed` (~0 tok)
- `reporters.py` — BaseReporter: starting, starting_round, ending_round, ending + 4 more (~458 tok)
- `resolvers.py` — ResolverException: iter_requirement, iter_parent, state (~5861 tok)
- `structs.py` — DirectedGraph: copy, add, remove, connected + 5 more (~1418 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/resolvelib/compat/

- `__init__.py` (~0 tok)
- `collections_abc.py` (~45 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/rich/

- `__init__.py` — Rich text and beautiful formatting in the terminal. (~1740 tok)
- `__main__.py` — ColorBox: make_test_card, comparison, iter_last (~2377 tok)
- `_cell_widths.py` — Auto generated by make_terminal_widths.py (~2917 tok)
- `_emoji_codes.py` (~36342 tok)
- `_emoji_replace.py` — do_replace (~304 tok)
- `_export_format.py` (~608 tok)
- `_extension.py` — load_ipython_extension (~76 tok)
- `_fileno.py` — get_fileno (~229 tok)
- `_inspect.py` — Inspect: sort_items, safe_getattr, get_object_types_mro, get_object_types_mro_as_strings + 1 more (~2770 tok)
- `_log_render.py` — Declares LogRender (~922 tok)
- `_loop.py` — loop_first, loop_last, loop_first_last (~354 tok)
- `_null_file.py` — NullFile: close, isatty, read, readable + 11 more (~397 tok)
- `_palettes.py` — Taken from https://en.wikipedia.org/wiki/ANSI_escape_code (Windows 10 column) (~2018 tok)
- `_pick.py` — pick_bool (~121 tok)
- `_ratio.py` — Edge: ratio_resolve, ratio_reduce, ratio_distribute (~1564 tok)
- `_spinners.py` (~4056 tok)
- `_stack.py` — Stack: top, push (~101 tok)
- `_timer.py` — timer (~120 tok)
- `_win32_console.py` — Light wrapper around the Win32 Console API - this module should only be imported on Windows (~6520 tok)
- `_windows_renderer.py` — legacy_windows_render (~796 tok)
- `_windows.py` — class: get_windows_console_features, get_windows_console_features (~550 tok)
- `_wrap.py` — words, divide_line (~951 tok)
- `abc.py` — Declares RichRenderable (~255 tok)
- `align.py` — Align: left, center, right, generate_segments + 2 more (~2963 tok)
- `ansi.py` — _AnsiToken: decode, decode_line, read (~1973 tok)
- `bar.py` — There are left-aligned characters for 1/8 to 7/8, but (~924 tok)
- `box.py` — Box: substitute, get_plain_headed_box, get_top, get_row + 1 more (~2909 tok)
- `cells.py` — Regex to match sequence of the most common character ranges (~1330 tok)
- `color_triplet.py` — ColorTriplet: hex, rgb, normalized (~302 tok)
- `color.py` — ColorSystem: system, is_system_defined, is_default, get_truecolor + 5 more (~5206 tok)
- `columns.py` — Columns: add_renderable, iter_renderables (~2038 tok)
- `console.py` — View: update, get (~28334 tok)
- `constrain.py` — Declares Constrain (~368 tok)
- `containers.py` — Renderables: append, append, extend, pop + 1 more (~1572 tok)
- `control.py` — Control: bell, home, move, get_codes + 8 more (~1894 tok)
- `default_styles.py` (~2310 tok)
- `diagnose.py` — report (~278 tok)
- `emoji.py` — NoEmoji: replace (~715 tok)
- `errors.py` — Declares ConsoleError (~184 tok)
- `file_proxy.py` — FileProxy: rich_proxied_file, write, flush, fileno (~481 tok)
- `filesize.py` — Functions for reporting filesizes. Borrowed from https://github.com/PyFilesystem/pyfilesystem2 (~717 tok)
- `highlighter.py` — Highlighter: highlight, highlight, highlight, highlight (~2739 tok)
- `json.py` — JSON: from_data (~1438 tok)
- `jupyter.py` — JupyterRenderable: escape, display, print (~930 tok)
- `layout.py` — View: get, update (~4000 tok)
- `live_render.py` — LiveRender: set_renderable, position_cursor, restore_cursor (~1048 tok)
- `live.py` — _RefreshThread: stop, run, is_started, get_renderable + 7 more (~4078 tok)
- `logging.py` — RichHandler: get_level_text, emit, render_message, render + 1 more (~3401 tok)
- `markup.py` — Tag: markup, escape, escape_backslashes, render + 1 more (~2415 tok)
- `measure.py` — Measurement: span, normalize, with_maximum, with_minimum + 3 more (~1516 tok)
- `padding.py` — Padding: indent, unpack (~1420 tok)
- `pager.py` — Pager: show, show (~237 tok)
- `palette.py` — Palette: match, get_color_distance (~970 tok)
- `panel.py` — Panel: fit, align_text (~3059 tok)
- `pretty.py` — from: install, display_hook (~10243 tok)
- `progress_bar.py` — Number of characters before 'pulse' animation repeats (~2331 tok)
- `progress.py` — SQLAlchemy: _TrackThread (~17059 tok)
- `prompt.py` — PromptError: ask, ask, ask, render_default + 8 more (~3230 tok)
- `protocol.py` — if: is_renderable, rich_cast (~398 tok)
- `py.typed` (~0 tok)
- `region.py` — Declares Region (~48 tok)
- `repr.py` — ReprError: auto, auto, auto, do_replace + 5 more (~1266 tok)
- `rule.py` — Declares Rule (~1314 tok)
- `scope.py` — render_scope, sort_items, test (~813 tok)
- `screen.py` — Declares Screen (~455 tok)
- `segment.py` — ControlType: cell_length, is_control, split_cells, line + 8 more (~6928 tok)
- `spinner.py` — Spinner: render, update (~1240 tok)
- `status.py` — Status: renderable, console, update, start + 1 more (~1264 tok)
- `style.py` — Style instances and style definitions are often interchangeable (~7736 tok)
- `styled.py` — Declares Styled (~360 tok)
- `syntax.py` — URL configuration (~10136 tok)
- `table.py` — class: copy, cells, flexible, grid (~11338 tok)
- `terminal_theme.py` — Declares TerminalTheme (~963 tok)
- `text.py` — Span: split, move, right_crop, extend + 7 more (~13516 tok)
- `theme.py` — Theme: config, from_file, read, push_theme + 1 more (~1080 tok)
- `themes.py` (~30 tok)
- `traceback.py` — URL configuration (~8440 tok)
- `tree.py` — Tree: add, make_guide (~2605 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/tomli/

- `__init__.py` — SPDX-License-Identifier: MIT (~114 tok)
- `_parser.py` — SPDX-License-Identifier: MIT (~6467 tok)
- `_re.py` — SPDX-License-Identifier: MIT (~841 tok)
- `_types.py` — SPDX-License-Identifier: MIT (~73 tok)
- `py.typed` — Marker file for PEP 561 (~7 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/truststore/

- `__init__.py` — Verify certificates using native system trust stores (~116 tok)
- `_api.py` — to: inject_into_ssl, extract_from_ssl, do_handshake, wrap_socket + 34 more (~2989 tok)
- `_macos.py` — Declares CFConst (~5031 tok)
- `_openssl.py` — candidates based on https://github.com/tiran/certifi-system-store by Christian Heimes (~664 tok)
- `_ssl_constants.py` — Hold on to the original class so we can create it consistently (~323 tok)
- `_windows.py` — Declares CERT_CONTEXT (~5112 tok)
- `py.typed` (~0 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/urllib3/

- `__init__.py` — add_stderr_logger, disable_warnings (~953 tok)
- `_collections.py` — RLock: clear, keys, pop, discard + 8 more (~3250 tok)
- `_version.py` — This file is protected via CODEOWNERS (~19 tok)
- `connection.py` — BaseSSLError: host, host, connect, putrequest + 4 more (~5800 tok)
- `connectionpool.py` — ConnectionPool: close (~11510 tok)
- `exceptions.py` — Base Exceptions (~2348 tok)
- `fields.py` — RequestField: guess_content_type, format_header_param_rfc2231, replacer, format_header_param_html5 + 3 more (~2452 tok)
- `filepost.py` — choose_boundary, iter_field_objects, iter_fields, encode_multipart_formdata (~698 tok)
- `poolmanager.py` — used: clear, connection_from_host, connection_from_context, connection_from_pool_key + 1 more (~5712 tok)
- `request.py` — RequestMethods: urlopen, request, request_encode_url, request_encode_body (~1912 tok)
- `response.py` — DeflateDecoder: decompress, decompress, flush, flush + 8 more (~8755 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/urllib3/contrib/

- `__init__.py` (~0 tok)
- `_appengine_environ.py` — is_appengine, is_appengine_sandbox, is_local_appengine, is_prod_appengine + 1 more (~274 tok)
- `appengine.py` — AppEnginePlatformWarning: urlopen (~3154 tok)
- `ntlmpool.py` — NTLMConnectionPool: urlopen (~1294 tok)
- `pyopenssl.py` — UnsupportedExtension: inject_into_urllib3, extract_from_urllib3, idna_encode, get_subj_alt_name + 5 more (~4881 tok)
- `securetransport.py` — inject_into_urllib3, extract_from_urllib3 (~9842 tok)
- `socks.py` — -*- coding: utf-8 -*- (~2028 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/urllib3/contrib/_securetransport/

- `__init__.py` (~0 tok)
- `bindings.py` — load_cdll (~5038 tok)
- `low_level.py` — Declares is (~3978 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/urllib3/packages/

- `__init__.py` (~0 tok)
- `six.py` — Utilities for writing code that runs on Python 2 and 3 (~9905 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/urllib3/packages/backports/

- `__init__.py` (~0 tok)
- `makefile.py` — -*- coding: utf-8 -*- (~405 tok)
- `weakref_finalize.py` — -*- coding: utf-8 -*- (~1527 tok)

## venv/lib/python3.13/site-packages/pip/_vendor/urllib3/util/

- `__init__.py` — For backwards compatibility, provide imports that used to be here. (~330 tok)
- `connection.py` — is_connection_dropped, create_connection, allowed_gai_family (~1401 tok)
- `proxy.py` — connection_requires_http_tunnel, create_proxy_ssl_context (~459 tok)
- `queue.py` — Declares LifoQueue (~143 tok)
- `request.py` — Pass as a value within ``headers`` to skip (~1142 tok)
- `response.py` — is_fp_closed, assert_header_parsing, is_response_to_head (~1003 tok)
- `retry.py` — with: DEFAULT_METHOD_WHITELIST, DEFAULT_METHOD_WHITELIST, DEFAULT_REDIRECT_HEADERS_BLACKLIST, DEFAULT_REDIRECT_HEADERS_BLACKLIST + 4 more (~6290 tok)
- `ssl_.py` — SSLContext: load_cert_chain, load_verify_locations, set_ciphers, wrap_socket + 6 more (~4908 tok)
- `ssl_match_hostname.py` — The match_hostname() function from Python 3.3.3, essential when using SSL. (~1646 tok)
- `ssltransport.py` — SSLTransport: fileno, read, recv, recv_into + 14 more (~1970 tok)
- `timeout.py` — The default socket timeout, used by httplib to indicate that no timeout was; specified by the user (~2906 tok)
- `url.py` — Url: hostname, request_uri, netloc, url + 2 more (~4085 tok)
- `wait.py` — NoWayToWaitForSocketError: select_wait_for_socket, poll_wait_for_socket, do_poll, null_wait_for_socket + 3 more (~1544 tok)

## venv/lib/python3.13/site-packages/python_dotenv-1.0.1.dist-info/

- `entry_points.txt` (~12 tok)
- `INSTALLER` (~2 tok)
- `LICENSE` — Project license (~415 tok)
- `METADATA` — Declares hint (~6176 tok)
- `RECORD` (~485 tok)
- `REQUESTED` (~0 tok)
- `top_level.txt` (~2 tok)
- `WHEEL` (~25 tok)
