import vwb_folder_utils as vfu


THOUSAND_GENOMES_CLI_OUTPUT = f"""├── Genomics (de5bf30a-78a6-4686-92e6-687b472b1475)
│   ├── Variant Files (d018eff8-bba1-4d59-b9e0-a7db7ed66422)
│   └── Aligned Files (f6cc00ad-9d66-4644-8543-7c3ced6bd63f)
└── Clinical (05f362fe-d205-44a3-b5a8-4ad6d242e8ac)
    └── Synthetic Data (d6e9058e-976f-4f51-9352-43abe59657b7)"""
        
THOUSAND_GENOMES_PARSED_TREE = [{'folder': 'Genomics', 'id': 'de5bf30a-78a6-4686-92e6-687b472b1475', 'depth': 1, 'children': [{'folder': 'Variant Files', 'id': 'd018eff8-bba1-4d59-b9e0-a7db7ed66422', 'depth': 2, 'children': []}, {'folder': 'Aligned Files', 'id': 'f6cc00ad-9d66-4644-8543-7c3ced6bd63f', 'depth': 2, 'children': []}]}, {'folder': 'Clinical', 'id': '05f362fe-d205-44a3-b5a8-4ad6d242e8ac', 'depth': 1, 'children': [{'folder': 'Synthetic Data', 'id': 'd6e9058e-976f-4f51-9352-43abe59657b7', 'depth': 2, 'children': []}]}]

class TestClass:
    
    def test_parse_tree_from_cli_output(self):
        expected = THOUSAND_GENOMES_PARSED_TREE
        assert expected == vfu.parse_tree(THOUSAND_GENOMES_CLI_OUTPUT)
        
    def test_parse_tree_with_no_folders(self):
        expected = []
        assert expected == vfu.parse_tree("")
        
    def test_get_folder_id(self):
        genomics_id = 'de5bf30a-78a6-4686-92e6-687b472b1475'
        variant_files_id = 'd018eff8-bba1-4d59-b9e0-a7db7ed66422'
        aligned_files_id = 'f6cc00ad-9d66-4644-8543-7c3ced6bd63f'
        synthetic_data_id = 'd6e9058e-976f-4f51-9352-43abe59657b7'
        # first in first list -- ├── Name
        assert genomics_id == vfu.get_folder_id('Genomics', THOUSAND_GENOMES_PARSED_TREE)
        # not last in not last nested list -- │(   )*├── Name
        assert variant_files_id == vfu.get_folder_id('Variant Files', THOUSAND_GENOMES_PARSED_TREE)
        # last in not-last nested list -- │(   )*└── Name
        assert aligned_files_id == vfu.get_folder_id('Aligned Files', THOUSAND_GENOMES_PARSED_TREE)
        # last in last nested list -- (   )*└── Name
        assert synthetic_data_id == vfu.get_folder_id('Synthetic Data', THOUSAND_GENOMES_PARSED_TREE)
        # no such folder exists
        assert None == vfu.get_folder_id("New Folder", THOUSAND_GENOMES_PARSED_TREE)
        
    def test_get_versions(self):