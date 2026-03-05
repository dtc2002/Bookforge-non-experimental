def validate_final_output(output):
    """Perform final voice/continuity validation on exported content"""
    
    # Check for empty output
    if not output:
        return {'status': 'error', 'message': 'Empty output'}
    
    # Check for excessive length
    if len(output) > 100000:
        return {'status': 'error', 'message': 'Output too large'}
    
    # Basic continuity check (example: ensure paragraphs are properly separated)
    if '\n\n' not in output:
        return {'status': 'error', 'message': 'Missing paragraph separators'}
    
    # Additional validation logic here
    
    return {'status': 'success', 'message': 'Validation passed'}

# Example usage
if __name__ == '__main__':
    sample_output = "This is a sample output\n\nThis is another paragraph."
    result = validate_final_output(sample_output)
    print(result['message'])