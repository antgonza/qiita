Checklist to send data to EBI-ENA
=================================

`Here <https://knightlab.ucsd.edu/wordpress/wp-content/uploads/2016/04/QiitaTemplate_20181218.xlsx>`__ you will find a document outlining these requirements, with examples, when possible.

For each preparation that needs to be uploaded to EBI-ENA we will check:

  1. Data processing

    a. Only datasets where raw sequences are available and linked to the preparation can be submitted. Studies where the starting point is a BIOM table cannot be submitted, since EBI is a sequence archive
    b. The data is processed and the owner confirms the data is correct:

      1. For target gene: data is demultiplexed (review split_library_log to make sure each sample has roughly the expected number of sequences) and there is at least a closed-reference (GG for 16S, Silva for 18S, UNITE for ITS) or trim/deblur artifacts. Trimming should be done with 90, 100 and 150 base pairs (preferred)
      2. For shotgun: data is uploaded via per_sample_FASTQ and processed using Shogun/utree. Remember to remove sequencing data for any human subject via `the HMP SOP <https://www.hmpdacc.org/hmp/doc/HumanSequenceRemoval_SOP.pdf>`__ or `the Knight Lab SOP <https://github.com/qiita-spots/qp-shogun/blob/master/notebooks/host_filtering.rst>`__

  2. Verify the sample information

    a. Check that the sample information file complies with `the current Qiita metadata format <https://qiita.ucsd.edu/static/doc/html/gettingstartedguide/index.html#sample-information-file>`__.
    b. Minimal information:

      1. *sample_name*
      2. *host_subject_id*
      3. *sample_type*
      4. *taxon_id* - needs to match *scientific_name* value
      5. *scientific_name* - needs to match *taxon_id* value - this is the name of the `metagenome <https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Tree&id=12908&lvl=3&srchmode=1&keep=1&unlock>`__ referenced in the column *taxon_id* and that the two values match.  Submission will not work if the user puts *host_scientific_name* or *host_taxid* instead.  Do not accept EBI null values. For null values use *scientific_name* “metagenome” and *taxon_id* “256318”
      6. *env_biome*, *env_feature*, *env_material*, *env_package*, for options `visit the ENVO section in <http://ols.wordvis.com/>`__
      7. *elevation*, *latitude*, *longitude*
      8. *empo_1*, *empo_2*, *empo_3*

    c. Extra minimal information for host associated studies:

      1. *host_body_habitat*, *host_body_site*, *host_body_product*
      2. *host_scientific_name*
      3. *host_common_name*
      4. *host_taxid*, `full list <https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi>`__
      5. *host_age*, *host_age_units*
      6. *host_height*, *host_height_units*
      7. *host_weight*, *host_weight_units*
      8. *host_body_mass_index* (human only)

    d. Double-check these fields:

      1. Check the date format, should be YYYY-MM-DD (hh:mm)
      2. Check null values
      3. Check that the values in each field make sense, for example that sex is not a numerical gradient, or that ph does not contain “male” or “female” values

  3. Verify the preparation information

    a. Check that the preparation information file complies with `the current Qiita metadata format <https://qiita.ucsd.edu/static/doc/html/gettingstartedguide/index.html#id1>`__
    b. Check that the correct Investigation type is selected on the prep info page
    c. Check for fill down errors in library_construction_protocol and target_subfragment; these are common.
    d. Minimal columns:

      1. *sample_name*
      2. *barcode*
      3. *primer* (include linker in this field)
      4. *platform*
      5. *experiment_design_description*
      6. *center_name*
      7. *center_project_name*
      8. *library_construction_protocol*
      9. *instrument_model*
      10. *sequencing_method*

    c. Additional minimal columns, if possible:

      1. *pcr_primers*
      2. *run_prefix*
      3. *run_center*
      4. *run_date*
      5. *target_gene*
      6. *target_subfragment*

  4. `EBI null values <http://www.ebi.ac.uk/ena/about/missing-values-reporting>`__ for use when data is not present:

    a. not applicable
    b. missing:

      1. not collected
      2. not provided
      3. restricted access
